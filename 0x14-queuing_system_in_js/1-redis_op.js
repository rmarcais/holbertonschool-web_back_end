import  { createClient, print } from 'redis';

const client = createClient();

client.on('error', (error) => console.log('Redis client not connected to the server: ' + error.toString()));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    print('Reply: ' + reply);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
