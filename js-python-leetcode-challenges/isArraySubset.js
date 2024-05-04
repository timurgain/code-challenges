/**
 * Given two arrays, return true if a one is subset for another, and false otherwise
 *
 * @param {array} source
 * @param {array} subset
 * @return {boolean}
 */

function isArraySubset(source, subset) {
  if (source.length < subset.length) return false
  for (let i = 0; i < subset.length; i++) {
    const index = source.indexOf(subset[i])
    if (index === -1) return false
    source.splice(index, 1)
  }
  return true
}


a = [2, 3, 5, 8, 14]
b = [5, 8, 2, 8]

console.log(isArraySubset(a, b))
