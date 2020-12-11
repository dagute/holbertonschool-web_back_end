export default function appendToEachArrayValue(array, appendString) {
  const aux = array;
  for (const value of array) {
    const index = array.indexOf(value);
    aux[index] = appendString + value;
  }

  return aux;
}
