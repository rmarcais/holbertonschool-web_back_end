const fs = require('fs');

module.exports = function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
  const [headerLine, ...lines] = data.split('\n').filter((line) => line.length > 0);
  const headers = headerLine.split(',');
  console.log(`Number of students: ${lines.length}`);
  const listObj = lines.map((line) => line.split(',')
    .reduce((object, currentValue, index) => ({
      ...object,
      [headers[index]]: currentValue,
    }), {}));
  const groupByField = listObj.reduce((res, currentValue) => {
    res[currentValue.field] = res[currentValue.field] || [];
    res[currentValue.field].push(currentValue.firstname);
    return res;
  }, {});
  Object.keys(groupByField).forEach((key) => {
    console.log(`Number of students in ${key}: ${groupByField[key].length}. List: ${groupByField[key].join(', ')}`);
  });
};
