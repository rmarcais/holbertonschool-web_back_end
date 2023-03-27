export default function cleanSet(set, startString) {
  if (startString === undefined || startString === '') {
    return '';
  }

  const result = [];

  for (const item of set) {
    if (item !== undefined && item.startsWith(startString)) {
      result.push(item.substring(startString.length));
    }
  }
  return result.join('-');
}
