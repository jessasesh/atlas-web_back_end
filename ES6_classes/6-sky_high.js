import Building from './5-building';
// Define a new class named SkyHighBuilding that extends the Building class
export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    // Check if the floors parameter is not a number
    if (typeof floors !== 'number') {
      // Throw a TypeError if floors is not a number
      throw TypeError('Floors must be a number');
    }
    // Call the constructor of the superclass (Building) with the sqft parameter
    super(sqft);
    // Initialize the _floors property with the floors parameter
    this._floors = floors;
  }

  // Getter to retrie value of _sqft property
  get sqft() {
    return this._sqft;
  }

  // Getter to retrie value of _flooor property
  get floors() {
    return this._floors;
  }

  // Warning message for specified floor
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
