export default class HolbertonCourse {
  constructor(name, length, students) {
    // Validators to check parameter types
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || students.some(student => typeof student !== 'string')) {
      throw TypeError('Students must be an array of strings');
    }

    // Initialize instance variables
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter and setter for the name attribute
  get name() {
    return this._name;
  }

  set name(x) {
    // Validator to ensure parameter type
    if (typeof x === 'string') {
      this._name = x;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  // Getter and setter for the length attribute
  get length() {
    return this._length;
  }

  set length(x) {
    // Validator to ensure parameter type
    if (typeof x === 'number') {
      this._length = x;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  // Getter and setter for the students attribute
  get students() {
    return this._students;
  }

  set students(x) {
    // Validator to ensure parameter type
    if (Array.isArray(x) && x.every(student => typeof student === 'string')) {
      this._students = x;
    } else {
      throw TypeError('Students must be an array of strings');
    }
  }
}
