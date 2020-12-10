export default function createIteratorObject(report) {
  const all = Object.values(report.allEmployees).reduce((a, b) => {
    a.push(...b);
    return a;
  }, []);
  let c = 0;
  return {
    [Symbol.iterator]: () => ({
      next() {
        if (c < all.length) {
          const aux = { data: all[c], done: false };
          c += 1;
          return aux;
        }
        return { data: null, done: true };
      },
    }),
  };
}
