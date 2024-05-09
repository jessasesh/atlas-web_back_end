export default class Building {
  constructor(sqft) {
    // Check if the constructor is called directly from Building or from a subclass
    if (
      this.constructor !== Building
      && typeof this.evacuationWarningMessage !== 'function'
    ) {
      // Throw an error if a subclass doesn't override evacuationWarningMessage method
      throw Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
    // Initialize the _sqft property with the provided value
    this._sqft = sqft;
  }
  // Getter method for accessing the _sqft property
  get sqft() {
    return this._sqft;
  }
}
