/**
 * Given a sentence, reverse the order of its words without affecting the order
 * of letters within a given word.
 *
 * @param {string} s
 * @returns {string}
 */

function reverseWords(s) {
  rev_arr = s.replace(/ +/, ' ').trim().split('').reverse()
  let first = 0;
  let second = 0;

  while (first < rev_arr.length) {
    while (second < rev_arr.length && rev_arr[second] !== " ") {
      second++
    }
    rev_arr = [].concat(
      rev_arr.slice(0, first), rev_arr.slice(first, second).reverse(),
      rev_arr.slice(second)
    )
    first = second + 1
    second = second + 1
  }
  return rev_arr.join('')
}

// main

const s = "You   are amazing  "
console.log(reverseWords(s))
