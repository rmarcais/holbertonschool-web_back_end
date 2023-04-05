module.exports = function calculateNumber(type, a, b) {
  if (typeof type !== 'string') {
    throw new TypeError('The type parameter must be a string');
  }
  const rounded_a = Math.round(a);
  const rounded_b = Math.round(b);
  if (type === 'SUM') {
    return rounded_a + rounded_b;
  } else if (type === 'SUBSTRACT') {
    return rounded_a - rounded_b;
  } else if (type === 'DIVIDE') {
      if (rounded_b === 0) {
        return 'Error';
      }
      return rounded_a / rounded_b;
  }
  it('should throw an error if argument type is not a string', () => {
    assert.throws(() => calculateNumber(true, 1, 2), {
      name: 'TypeError',
      message: 'The type parameter must be a string',
    });
    assert.throws(() => calculateNumber(1, 1, 5), {
      name: 'TypeError',
      message: 'The type parameter must be a string',
    });
  });
};
