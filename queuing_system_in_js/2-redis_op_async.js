import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Promisify the method
const getAsync = promisify(client.get).bind(client);

// Function to set a new school in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await getAsync(schoolName);
    console.log(`Value for ${schoolName}: ${reply}`);
  } catch (err) {
    console.log(`Error retrieving value for ${schoolName}: ${err}`);
  }
};

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
