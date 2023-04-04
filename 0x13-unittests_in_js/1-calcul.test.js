const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber with SUM', function() {
  it('Checks 1 + 3', function() {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
  });
  it('Checks 1 + 3.7', function() {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('Checks 1.2 + 3.7', function() {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('Checks 1.5 + 3.7', function() {
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('Checks -3 + 1.2', function() {
    assert.equal(calculateNumber('SUM', -3, 1.2), -2);
  });
});

describe('calculateNumber with SUBSTRACT', function() {
  it('Checks 3 - 1', function() {
    assert.equal(calculateNumber('SUBSTRACT', 3, 1), 2);
  });
  it('Checks 1 - 3', function() {
    assert.equal(calculateNumber('SUBSTRACT', 1, 3), -2);
  });
  it('Checks 1.2 - 3.7', function() {
    assert.equal(calculateNumber('SUBSTRACT', 1.2, 3.7), -3);
  });
  it('Checks 3.7 - 1.5', function() {
    assert.equal(calculateNumber('SUBSTRACT', 3.7, 1.5), 2);
  });
  it('Checks 0.1 - 0.1', function() {
    assert.equal(calculateNumber('SUBSTRACT', 0.1, 0.1), 0);
  });
});

describe('calculateNumber with DIVIDE', function() {
  it('Checks 3 / 1', function() {
    assert.equal(calculateNumber('DIVIDE', 3, 1), 3);
  });
  it('Checks 3.5 / 2.1', function() {
    assert.equal(calculateNumber('DIVIDE', 3.5, 2.1), 2);
  });
  it('Checks 1.9 / 4.1', function() {
    assert.equal(calculateNumber('DIVIDE', 1.9, 4.1), 0.5);
  });
  it('Checks 3 / 0', function() {
    assert.equal(calculateNumber('DIVIDE', 3, 0), 'Error');
  });
  it('Checks 0.1 / 0.1', function() {
    assert.equal(calculateNumber('DIVIDE', 0.1, 0.1), 'Error');
  });
});

describe('calculateNumber with a wrong type', function() {
  it('Checks with NOPE as type', function() {
    assert.equal(calculateNumber('NOPE', 3, 1), 'Error');
  });
});