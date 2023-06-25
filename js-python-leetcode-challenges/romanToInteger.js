/*
Given a roman numeral, convert it to an integer.
*/

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const dict = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  return s.split('').reduce((result, _, index, arr) => {
    if (index > 0 && dict[arr[index-1]] < dict[arr[index]]) {
      return result
    }
    if (index === arr.lenth - 1) {
      return result += dict[arr[index]]
    }
    if (dict[arr[index]] < dict[arr[index+1]]) {
      return result += dict[arr[index+1]] - dict[arr[index]]
    } else {
      return result += dict[arr[index]]
    }
  }, 0);
};

const res = romanToInt("MCMXCIV"); // 1994
console.log(res);
