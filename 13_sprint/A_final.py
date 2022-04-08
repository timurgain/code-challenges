"""A. Search in a broken rounded sorted array."""


def broken_search(nums: list, target: int):
    if len(nums) == 0:
        return -1
    mid = len(nums) // 2

    # run binary search if an array part is sorted, return result if found
    result = -1
    last = len(nums) - 1
    if nums[0] < nums[mid]:
        result = binary_search(nums[0:mid], target)
    if nums[mid] < nums[last] and result == -1:
        result = binary_search(nums[mid:last+1], target)
        result += mid if result > -1 else result
    if result > -1:
        return result

    # else repeat in recursion searching sorted part of array
    if nums[0] > nums[mid]:
        return broken_search(nums[0:mid],  target)
    if nums[mid] > nums[last] and result == -1:
        return broken_search(nums[mid:last],  target)


def binary_search(nums: list, target: int):
    if len(nums) == 0:
        return -1

    mid = len(nums) // 2
    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        return binary_search(nums[:mid], target)
    if nums[mid] < target:
        result = binary_search(nums[mid+1:], target)
        return result + mid + 1 if result > -1 else -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 6, 7, 12]
    assert broken_search(arr, 1) == 4


test()
