import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// Store values inbhash
const cities = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

Object.entries(cities).forEach(([city, value]) => {
  redisClient.hSet('HolbertonSchools', city, value, print);
});

redisClient.hGetAll('HolbertonSchools', (err, result) => {
  if (err) {
    console.log(`Error retrieving hash: ${err}`);
  } else {
    console.log(result);
  }
  redisClient.quit();
});
