export default function createReportObject(employeesList) {
  const allEmployees = {};

  for (const [dep, employees] of Object.entries(employeesList)) {
    allEmployees[dep] = [...employees];
  }
  const reportObject = {
    allEmployees,
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return reportObject;
}
