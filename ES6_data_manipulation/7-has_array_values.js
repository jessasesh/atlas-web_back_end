// Function to check if all values in the array are present in the set
export default function hasValuesFromArray(set, array) {
  return array.every((i) => set.has(i));
}
