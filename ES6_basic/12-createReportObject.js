export default function createReportObject(employeesList) {
  //Create object to return
  const empReport = {
    allEmployees: {
      ...employeesList,
    },
    //Second thing to be stored in the object
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };

  return empReport;
}
