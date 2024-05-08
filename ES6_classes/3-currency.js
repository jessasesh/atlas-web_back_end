export default class Currency {
  constructor(code, name) {
    this._code = '';
    this._name = '';

    // Validate and assign values
    this.code = code;
    this.name = name;
  }

  // Getter and setter for the code attribute
  get code() {
    return this._code;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode;
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

  // Method to display full currency information
  displayFullCurrency() {
    return `${this.name} (${this.code})`; // Corrected to use getters
  }
}
