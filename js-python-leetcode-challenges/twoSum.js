/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

function twoSum(nums, target) {
    const memo = {};
    for (let i = 0; i < nums.length; i++) {
        const need = target - nums[i]
        if (need in memo) {
            return [memo[need], i]
        }
        memo[nums[i]] = i;
    }
    return -1    
};


console.log(twoSum([2,7,11,15], 9))