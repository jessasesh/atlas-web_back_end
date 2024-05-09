export default function cleanSet(set, startString) {
  // Initialize an empty string to store the result
  let result = '';

  // Check if startString is not provided or not a string
  if (!startString || typeof startString !== 'string') {
    // If so, return an empty string
    return '';
  }

  // Iterate through each item in the set
  for (const item of set) {
    // Check if the item starts with the provided startString
    if (item.startsWith(startString)) {
      // If so, append the substring of the item (after startString) followed by '-'
      result += `${item.substring(startString.length)}-`;
    }
  }

  // Return the result string, removing the trailing '-' character
  return result.slice(0, -1);
}
