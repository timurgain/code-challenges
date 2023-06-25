/**
 * Takes a string and determines whether or not it is a palindrome.
 * @param {string} s
 * @returns {boolean}
 */

function isPalindrome(s) {
  if (s.length < 1) return false;
  for (let i = 0; i < s.length; i++) {
    if (i < Math.abs(-1-i)) {
      const one = s[i]
      const two = s.at(-1-i)
      if (one !== two) return false;
    }
  }
  return true
}

// main

const s = "moomk"
console.log(isPalindrome(s))
