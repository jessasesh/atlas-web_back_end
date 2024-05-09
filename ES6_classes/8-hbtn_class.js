export default class HolbertonClass {
  // Constructor with attributes
  constructor(size, location) {
    // Number validator
    if (typeof size !== 'number') {
      throw TypeError('Size must be a number');
    }
    // String validator
    if (typeof location !== 'string') {
      throw TypeError('Location must be a string');
    }
    // Asssign size parameter to _size property
    this._size = size;
    // Assign location parameter to _location property
    this._location = location;
  }
  // Return size value of object 
  retrieveSize() {
    return this._size;
  }
  // Return location string of object
  retrieveLocation() {
    return this._location;
  }
}
