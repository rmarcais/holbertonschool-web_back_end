import kue from 'kue';

const queue = kue.createQueue();

const data = {
  phoneNumber: '0612141617',
  message: 'Hello World !',
}

const job = queue.create('push_notification_code', data).save((error) => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
