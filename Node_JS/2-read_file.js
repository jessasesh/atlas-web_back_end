const fs = require('fs');

function countStudents(filePath) {
  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      console.log('Cannot load the database');
      return;
    }

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

    Object.entries(studentsByField).forEach(([field, names]) => {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    });
  });
}

module.exports = countStudents;
