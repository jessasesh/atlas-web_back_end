// Function to extract student IDs from array of student objects
export default function getListStudentIds(array) {
  // Array validator
  if (!Array.isArray(array)) return [];
  // Use map method to create new array containt only IDs of student
  return array.map((i) => i.id);
}
