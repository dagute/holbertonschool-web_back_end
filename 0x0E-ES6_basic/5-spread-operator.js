export default function concatArrays(array1, array2, string) {
  const ret = [...array1, ...array2, ...string];
  return ret;
}
