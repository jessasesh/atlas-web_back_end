const http = require('http');

// Request handler function
const requestHandler = (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!\n');
};

const app = http.createServer(requestHandler);

const PORT = 1245;
const HOST = 'localhost';

// Listen for incoming requests
app.listen(PORT, HOST, () => {
    // Fancy print statements
  console.log(`Server is running at http://${HOST}:${PORT}`);
});

module.exports = app;
