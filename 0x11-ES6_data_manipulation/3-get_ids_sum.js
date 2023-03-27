export default function getStudentIdsSum(array) {
  return array.reduce((sum, currentValue) => sum + currentValue.id, 0);
}
