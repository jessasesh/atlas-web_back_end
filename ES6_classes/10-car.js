export default class Car {
  // Constructor with attributes
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Static getter for Symbol.species property
  static get [Symbol.species]() {
    return this;
  }

  // Methid to clone car instance
  cloneCar() {
    // Retrieve the Species class
    const Species = this.constructor[Symbol.species];
    // Create new instance of Species class with same parameters
    return new Species(this._brand, this._motor, this._color);
  }
}
