export default function createIteratorObject(report) {
  const array = [];
  for (const employees of Object.values(report.allEmployees)) {
    array.push(...employees);
  }
  const iterator = array[Symbol.iterator]();

  return iterator;
}
