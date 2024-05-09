// Define a class named Airport
export default class Airport {
  // Initialize Airport object with a name and a code
  constructor(name, code) {
    // String validator
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    // String validator
    if (typeof code !== 'string') {
      throw TypeError('Code must be a string');
    }
    // Assign name parameter to _name property
    this._name = name;
    // Assign code parameter to _code property
    this._code = code;
  }

  // Method to return airport code
  toString() {
    return `[object ${this._code}]`;
  }
}
