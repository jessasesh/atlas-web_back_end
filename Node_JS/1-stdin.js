const readline = require('readline');

const inputSession = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

inputSession.question('Welcome to Holberton School, what is your name?\n', (inputName) => {
  console.log(`Your name is: ${inputName}`);
  console.log('This important software is now closing');
  inputSession.close();
});
