export default function getNeighborhoodsList() {
  // Initialize sanFranciscoNeighborhoods array
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  // Define addNeighborhood method using arrow function
  this.addNeighborhood = (newNeighborhood) => {
    // Access sanFranciscoNeighborhoods using 'this'
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    // Return updated sanFranciscoNeighborhoods array
    return this.sanFranciscoNeighborhoods;
  };
}