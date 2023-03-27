export default function updateStudentGradeByCity(array, city, newGrades) {
  return array
    .filter((item) => item.location === city)
    .map((item) => {
      const grade = newGrades.find((element) => element.studentId === item.id);
      return {
        ...item,
        grade: grade === undefined ? 'N/A' : grade.grade,
      };
    });
}
