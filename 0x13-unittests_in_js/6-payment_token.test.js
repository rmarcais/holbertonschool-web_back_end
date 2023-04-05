const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('Tests the result of getPaymentTokenFromAPI(true)', function(done) {
    getPaymentTokenFromAPI(true).then((result) => {
        assert.deepStrictEqual(result, { data: 'Successful response from the API' });
        done();
    });
  });
});
