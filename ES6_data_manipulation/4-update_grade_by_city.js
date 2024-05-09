// Function that filters and maps students based on location and grades
export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // Map over the studentList to update grades
  const updatedStudentList = studentList.map((item) => {
    // Find the new grade for the current student
    const newGrade = newGrades.find((grade) => grade.studentId === item.id);
    // Assign the new grade if found, otherwise assign 'N/A'
    const grade = newGrade ? newGrade.grade : 'N/A';
    // Return a new object with updated grade
    return { ...item, grade };
  });

  // Filter the updatedStudentList to get students in the specified city
  const sortedStudentList = updatedStudentList.filter((item) => item.location === city);

  return sortedStudentList;
}
