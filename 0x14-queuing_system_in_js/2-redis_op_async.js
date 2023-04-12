import  { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (error) => console.log('Redis client not connected to the server: ' + error.toString()));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    print('Reply: ' + reply);
  });
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const result = await get(schoolName);
  console.log(result);
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
console.log('hello')