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

describe('Cart page', () => {
  const url = 'http://localhost:7865/cart/12';
  const wrongUrl = 'http://localhost:7865/cart/hello';
  it('Checks correct status code when :id is a number', (done) => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it('Checks the body when :id is a number', (done) => {
    request(url, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });
  it('Checks correct status code when :id is not a number', (done) => {
    request(wrongUrl, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
  it('Checks the body when :id is not a number', (done) => {
    request(wrongUrl, (error, response, body) => {
      expect(body).to.equal('');
      done();
    });
  });
});

describe('/login endpoint', () => {
  const url = 'http://localhost:7865/login';
  const options = {
    url: url,
    form: {
      userName: 'Betty'
    }
  };
  it('Checks the status code', (done) => {
    request.post(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it('Checks the body', (done) => {
    request.post(options, (error, response, body) => {
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});

describe('/available_payments endpoint', () => {
  const url = 'http://localhost:7865/available_payments';
  it('Checks the status code', (done) => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it('Checks the body', (done) => {
    request(url, (error, response, body) => {
      expect(body).to.deep.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}');
      done();
    });
  });
});
