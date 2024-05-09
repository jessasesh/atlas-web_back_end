export default function getStudentIdsSum(array) {
  // Use the map method to extract the IDs from the studentList
  // Then, use the reduce method to calculate the sum of the IDs
  const studentIdsum = array.map((item) => item.id)
    .reduce((total, studentID) => total + studentID, 0);

  return studentIdsum;
}
