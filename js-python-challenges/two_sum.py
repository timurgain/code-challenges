"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """Time O(n), memory O(n)."""
    memo = {}
    for index, current in enumerate(nums):
        need = target - current
        if need in memo.keys():
            return [memo[need], index]
        if current not in memo.keys():
            memo.update({current: index})
    return -1

# def two_sum(nums: List[int], target: int) -> List[int]:
#     """Time O(n^2), memory O(1)."""
#     for i, first in enumerate(nums):
#         for j, second in enumerate(nums[i+1:]):
#             if first + second == target:
#                 return [i, j+i+1]
#     return -1


if __name__ == '__main__':
    print(two_sum([2,7,11,15], 9))
    print(two_sum([3,2,4], 6))
