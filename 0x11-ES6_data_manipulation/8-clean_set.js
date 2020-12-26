export default function cleanSet(set, startString) {
  let finalString = '';
  if (!startString || !startString.length)
    return finalString;
  set.forEach((item) => {
    if (item && item.startsWith(startString))
      finalString += `${item.slice(startString.length)}-`;
  });

  return finalString.slice(0, finalString.length - 1);
}
