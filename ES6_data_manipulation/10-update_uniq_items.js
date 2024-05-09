export default function updateUniqueItems(oldMap) {
  // Check if oldMap is not an instance of Map
  if (!(oldMap instanceof Map)) {
    throw Error('Cannot process');
  }

  // Iterate through each key-value pair in the map
  for (const [item, itemValue] of oldMap) {
    // Check if the value is equal to 1
    if (itemValue === 1) {
      // If so, update the value to 100
      oldMap.set(item, 100);
    }
  }
  // Return updated map
  return oldMap;
}
