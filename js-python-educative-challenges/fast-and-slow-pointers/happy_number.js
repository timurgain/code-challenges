// Write an algorithm to determine if a number is a happy number.

// We use the following process to check if a given number is a happy number:
//     - Starting with the given number n, replace the number with the sum of the squares of its digits.
//     - Repeat the process until:
//         The number equals 1, which will depict that the given number is a happy number.
//         It enters a cycle, which will depict that the given number n is not a happy number.

// Return TRUE if n is a happy number, and FALSE if not.

/**
 * @param {number} n
 * @returns {number}
 */

function sumSqueredDigits(n) {
  res = 0;
  while (n > 0) {
    res += Math.pow(n % 10, 2)
    n = Math.floor(n / 10)
  }
  return res
}

/**
 * @param {number} n
 * @returns {boolean}
 */

function isHappyNumber(n) {
  let slow = n
  let fast = sumSqueredDigits(n)
  while (slow !== fast && fast !== 1) {
    slow = sumSqueredDigits(slow)
    fast = sumSqueredDigits(sumSqueredDigits(fast))
  }
  if (fast === 1) return true;
  return false;
}

// main

const n = 13
res = isHappyNumber(n)
console.log(res)
