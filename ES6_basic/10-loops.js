export default function appendToEachArrayValue(array, appendString) {
  // Loop through each value in the array using for...of loop
  for (let value of array) {
    // Concatenate appendString to each value
    value = appendString + value;
  }

  return array;
}
