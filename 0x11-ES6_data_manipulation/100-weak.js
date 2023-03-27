export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const count = weakMap.get(endpoint);
  weakMap.set(endpoint, count === undefined ? 1 : count + 1);

  if (count + 1 >= 5) {
    throw new Error('Endpoint load is high');
  }
}
