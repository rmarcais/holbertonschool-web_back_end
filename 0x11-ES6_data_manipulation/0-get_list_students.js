export default function getListStudents() {
  const array = [];

  const person1 = { id: 1, firstName: 'Guillaume', location: 'San Francisco' };
  const person2 = { id: 2, firstName: 'James', location: 'Columbia' };
  const person3 = { id: 5, firstName: 'Serena', location: 'San Francisco' };

  array.push(person1, person2, person3);

  return array;
}
