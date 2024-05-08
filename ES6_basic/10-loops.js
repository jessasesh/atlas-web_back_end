export default function appendToEachArrayValue(array, appendString) {
  const updatedArray = [];

  // Loop through each value in the array using for...of loop
  for (const value of array) {
    // Concatenate appendString to each value
    updatedArray.push(appendString + value);
  }
  return updatedArray;
}
