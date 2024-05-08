export default function createEmployeesObject(departmentName, employees) {
  const empInfo = {};
  empInfo[departmentName] = employees;
  return empInfo;
}
