"""Given an array of integers, nums, and an integer value, target,
    determine if there are any three integers in nums
    whose sum is equal to the target"""


def find_sum_of_three(nums: list[int], target: int) -> bool:
    if len(nums) < 3:
        return False
    sorted_nums = sorted(nums)

    for i in range(len(sorted_nums)-1):
        small_idx = i + 1
        big_idx = len(sorted_nums) - 1

        while small_idx < big_idx:
            res = sorted_nums[i] + sorted_nums[small_idx] + sorted_nums[big_idx]
            if res == target:
                return True
            if res < target:
                small_idx += 1
            if res > target:
                big_idx -= 1
    return False

if __name__ == '__main__':
    nums = [3,7,1,2,8,4,5]
    target = 10
    print(find_sum_of_three(nums, target))
