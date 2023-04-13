import express from 'express';
import  { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const client = createClient();
client.on('error', (error) => console.log('Redis client not connected to the server: ' + error.toString()));

function reserveSeat(number) {
    client.set('available_seats', number, (error) => {
        if (error) throw error;
    });
}
reserveSeat(50);

async function getCurrentAvailableSeats() {
    const asyncGet = promisify(client.get).bind(client);
    const availableSeats = await asyncGet('available_seats');
    return availableSeats;
}

let reservationEnabled = true;

const queue = kue.createQueue();

const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.send({"numberOfAvailableSeats":availableSeats});
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        res.send({ "status": "Reservation are blocked" });
    } else {
        const jobData = { block: 112, seat: 33 };
        const job = queue.create('reserve_seat', jobData)
        .on('complete', () => {
          console.log(`Seat reservation job ${job.id} completed`);
        })
        .on('failed', (error) => {
          console.log(`Seat reservation job ${job.id} failed: ${error.toString()}`);
        });
        job.save((error) => {
            if (!error) {
                res.send({ "status": "Reservation in process" });
            } else {
                res.send({ "status": "Reservation failed" });
            }
        });
    }
});

app.get('/process', (req, res) => {
    res.send({ "status": "Queue processing" });
    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();
        if (availableSeats < 1) {
            done(Error('Not enough seats available'));
        } else {
            reserveSeat(availableSeats - 1);
            if (availableSeats - 1 === 0) reservationEnabled = false;
            done();
        }
    });
});

app.listen(port, () => {
    console.log('API available on localhost port 1245');
});
