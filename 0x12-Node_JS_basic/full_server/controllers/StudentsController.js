import readDatabase from '../utils';

const DB = process.argv[2];

export default class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(DB).then((result) => {
      response.write('This is the list of our students');
      Object.keys(result).sort().forEach((key) => {
        response.write(`\nNumber of students in ${key}: ${result[key].length}. List: ${result[key]}`);
      });
      response.end();
    }).catch((error) => {
      response.status(500);
      response.send(error.message);
    });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500);
      response.send('Major parameter must be CS or SWE');
    } else {
      readDatabase(DB).then((result) => {
        response.send(`List: ${result[major]}`);
      }).catch((error) => {
        response.status(500);
        response.send(error.message);
      });
    }
  }
}
