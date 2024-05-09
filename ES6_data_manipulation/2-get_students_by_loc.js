export default function getStudentsByLocation(array, city) {
  const filteredList = array.filter((item) => item.location === city);

  return filteredList;
}
