export default class HolbertonCourse {
  constructor(name, length, students) {
    // Verify the type of attributes during object creation
    if (typeof name !== 'string' || typeof length !== 'number' || !Array.isArray(students)) {
      throw new Error('Invalid parameter types');
    }

    // Initialize the attributes
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter and setter for the name attribute
  get name() {
    return this._name;
  }
  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  // Getter and setter for the length attribute
  get length() {
    return this._length;
  }
  set length(newLength) {
    if (typeof newLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = newLength;
  }

  // Getter and setter for the students attribute
  get students() {
    return this._students;
  }
  set students(newStudents) {
    if (!Array.isArray(newStudents) || newStudents.some(student => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = newStudents;
  }
}
