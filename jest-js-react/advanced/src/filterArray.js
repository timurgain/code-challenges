export function filterArray(array, callback) {
  let newArray = [];
  array.forEach((item) => {
    if (callback(item)) newArray.push(item);
  });
  return newArray;
}
