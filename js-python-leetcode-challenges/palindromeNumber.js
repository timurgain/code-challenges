/*
Given an integer x, return true if x is a palindrome, and false otherwise
*/

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  if (x < 0) return false;
  if (x < 10) return true;

  let sourceNum = x;
  let mirrorNum = 0;
  while (x > 0) {
    mirrorNum = mirrorNum*10 + x%10
    x = Math.floor(x/10);
  }
  return (mirrorNum === sourceNum) ? true : false;
};


console.log(isPalindrome(12344331))
