export default function groceriesList() {
  const gList = {
    Apples: 10,
    Tomatoes: 10,
    Pasta: 1,
    Rice: 1,
    Banana: 5,
  };

  const map = new Map();

  for (const [key, value] of Object.entries(gList)) {
    map.set(key, value);
  }

  return map;
}
