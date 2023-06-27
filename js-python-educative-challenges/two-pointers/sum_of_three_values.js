/**
 * Given an array of integers, nums, and an integer value, target, determine
 * if there are any three integers in nums whose sum is equal to the target
 *
 * @param {Array<number>} nums
 * @param {number} target
 * @returns {boolean}
 */

function sumOfThree(nums, target) {
  if (nums.length < 3) return false;
  const sortedNums = nums.slice().sort((a, b) => a > b ? 1 : -1);

  for (i = 0; i < sortedNums.length - 1; i++) {
    let smallIndex = i + 1
    let bigIndex = sortedNums.length - 1
    while (smallIndex < bigIndex) {
      const res = sortedNums[i] + sortedNums[smallIndex] + sortedNums[bigIndex]
      if (res === target) return true;
      if (res < target) smallIndex++;
      if (res > target) bigIndex--;
    }
  }
  return false;
}

// main

const nums = [3,7,1,2,8,4,5]
const target = 10
console.log(sumOfThree(nums, target))
