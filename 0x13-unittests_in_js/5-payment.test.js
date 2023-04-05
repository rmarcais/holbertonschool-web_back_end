const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
    let log;

    beforeEach(function() {
        log = sinon.spy(console, 'log');
    });
    afterEach(function() {
        log.restore();
      });
    it('Calls sendPaymentRequestToAPI with 100, and 20', function() {
        const totalAmount = 100;
        const totalShipping = 20

        sendPaymentRequestToApi(totalAmount, totalShipping);
        
        sinon.assert.calledOnce(log);
        sinon.assert.calledWith(log, 'The total is: 120');
    });
    it('Calls sendPaymentRequestToAPI with 10, and 10', function() {
        const totalAmount = 10;
        const totalShipping = 10

        sendPaymentRequestToApi(totalAmount, totalShipping);
        
        sinon.assert.calledOnce(log);
        sinon.assert.calledWith(log, 'The total is: 20');
    });
});
