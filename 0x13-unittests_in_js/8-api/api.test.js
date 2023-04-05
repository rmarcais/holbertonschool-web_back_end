const chai = require('chai');
const request = require('request');
const { expect } = chai;

describe('Index page', () => {
  const url = 'http://localhost:7865/';
  it('Checks the status code', (done) => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it('Checks the body', (done) => {
    request(url, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
