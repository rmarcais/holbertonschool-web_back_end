const Utils = {
  calculateNumber: function (type, a, b) {
    if (type === 'SUM') {
        return Math.round(a) + Math.round(b);
    } else if (type === 'SUBTRACT') {
        return Math.round(a) - Math.round(b);
    } else if (type === 'DIVIDE') {
        return Math.round(b) !== 0 ? Math.round(a) / Math.round(b): 'Error';
    }
  }
}

module.exports = Utils;
