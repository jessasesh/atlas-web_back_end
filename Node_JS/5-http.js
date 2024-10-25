const http = require('http');
const fs = require('fs');
const path = require('path');

// Function to read students from CSV
const readStudentsFromCSV = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, data) => {
      if (error) return reject(new Error('Cannot load the database'));

      const students = data.trim().split('\n').slice(1)
        .reduce((acc, line) => {
          const [firstName, , , field] = line.split(',');
          if (firstName && field) {
            acc[field] = acc[field] || [];
            acc[field].push(firstName);
          }
          return acc;
        }, {});

      resolve(students);
    });
  });
};

// Create server
const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.writeHead(200);
    res.end('Hello Holberton School!\n');
  } else if (req.url === '/students') {
    try {
      const students = await readStudentsFromCSV(path.join(__dirname, 'database.csv'));
      let response = 'This is the list of our students\n';

      for (const [field, names] of Object.entries(students)) {
        response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      res.writeHead(200);
      res.end(response);
    } catch (error) {
      res.writeHead(500);
      res.end(error.message);
    }
  } else {
    res.writeHead(404);
    res.end('Not Found\n');
  }
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});

module.exports = app;
