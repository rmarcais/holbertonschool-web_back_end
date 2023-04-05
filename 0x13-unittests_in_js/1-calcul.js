module.exports = function calculateNumber(type, a, b) {
  if (typeof type !== 'string') {
    throw new TypeError('Type must be a string');
  }
  if (type === 'SUM') {
    return Math.round(a) + Math.round(b);
  } else if (type === 'SUBSTRACT') {
    return Math.round(a) - Math.round(b);
  } else if (type === 'DIVIDE') {
    return Math.round(b) !== 0 ? Math.round(a) / Math.round(b): 'Error';
  }
};
