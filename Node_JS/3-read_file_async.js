// Task 3 - Read CSV file async

const fs = require('fs');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
      } else {
        const entries = data.trim().split('\n').slice(1);
        const totalStudents = entries.length;

        console.log(`Number of students: ${totalStudents}`);

        const studentsByField = {};

        entries.forEach((entry) => {
          const [firstName, , , field] = entry.split(',');

          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }
          studentsByField[field].push(firstName);
        });

        let result = `Number of students: ${totalStudents}\n`;

        Object.entries(studentsByField).forEach(([field, names]) => {
          console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
          result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        });

        resolve(result);
      }
    });
  });
}

module.exports = countStudents;
