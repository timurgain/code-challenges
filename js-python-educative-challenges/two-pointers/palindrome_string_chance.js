// Write a function that takes a string as input and checks whether it can be
//  a valid palindrome by removing at most one character from it.

/**
 * @param {string} s
 * @returns {bool}
 */

function isPalindromeSlice(s) {
  if (s.length < 1) return false;
  let [left, right] = [0, s.length - 1]
  while (left < right) {
    if (s[left] !== s[right]) return false;
    left++;
    right--;
  }
  return true;
}


/**
 * @param {string} s
 * @returns {bool}
 */

function couldBePalindrome(s) {
  if (s.length < 1) return false;
  let [left, right, mismatch] = [0, s.length - 1, 0]
  while (left < right) {
    if (s[left] === s[right]) {
      left++;
      right--;
    } else {
      mismatch++;
      if (mismatch > 1) return false;
      if (isPalindromeSlice(s.slice(left, right))) return true;
      if (isPalindromeSlice(s.slice(left+1, right+1))) return true;
    }
  }
  return true;
}


// main

const s = 'abcdedadedecba'  // abc dedaded (e) cba
const res = couldBePalindrome(s)
console.log(res)
