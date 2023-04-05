module.exports = function calculateNumber(type, a, b) {
  if (typeof a === 'undefined' || typeof b === 'undefined' || typeof type === 'undefined') {
    throw new Error('Missing arguments');
  }

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
};
