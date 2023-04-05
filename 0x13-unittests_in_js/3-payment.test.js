const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
    it('Validates the usage of the Utils function', function() {
        const calculate = sinon.spy(Utils, 'calculateNumber');

        sendPaymentRequestToApi(100, 20);

        calculate.restore();
        sinon.assert.calledOnce(calculate);
        sinon.assert.calledWith(calculate, 'SUM', 100, 20);
    });
});
