const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
      } else {
        const [headerLine, ...lines] = data.split('\n').filter((line) => line.length > 0);
        const headers = headerLine.split(',');
        const result = [];

        let message = `Number of students: ${lines.length}`;
        console.log(message);
        result.push(message);

        const listObj = lines.map((line) => line.split(',').reduce((object, currentValue, index) => Object.assign(object, { [headers[index]]: currentValue }), {}));

        const groupByField = listObj.reduce((res, currentValue) => {
          res[currentValue.field] = res[currentValue.field] || [];
          res[currentValue.field].push(currentValue.firstname);
          return res;
        }, {});
        Object.keys(groupByField).forEach((key) => {
          message = `Number of students in ${key}: ${groupByField[key].length}. List: ${groupByField[key].join(', ')}`;
          console.log(message);
          result.push(message);
        });
        resolve(result);
      }
    });
  });
}

module.exports = countStudents;
