const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
    it('Validates the usage of the Utils function', function() {
        const calculate = sinon.spy(Utils, 'calculateNumber');
        const totalAmount = 100;
        const totalShipping = 20

        sendPaymentRequestToApi(totalAmount, totalShipping);

        calculate.restore();
        sinon.assert.calledOnce(calculate);
        sinon.assert.calledWith(calculate, 'SUM', totalAmount, totalShipping)
    });
});
