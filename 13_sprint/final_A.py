"""A. Поиск в сломанном массиве / Search in a broken rounded sorted array
ID принятого решения в Яндекс.Контест: 67073139."""


def handle_sorted_part(nums: list, target: int, left=None, right=None) -> int:
    """Discovers sorted part of array and sends it to binary search."""
    # array pointers
    left = 0 if left is None else left
    right = len(nums) - 1 if right is None else right

    # base cases
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if left == right:
        return -1
    result = -1

    # array part is sorted then binary search
    if nums[left] <= nums[mid] and nums[left] <= target <= nums[mid]:
        return binary_search(nums, target, 0, mid)
    if nums[mid+1] <= nums[right] and nums[mid+1] <= target <= nums[right]:
        return binary_search(nums, target, mid + 1, right + 1)

    # else recursion searching sorted part of array
    if nums[left] > nums[mid]:
        result = handle_sorted_part(nums, target, left, mid)
    if nums[mid] > nums[right] and result == -1:
        result = handle_sorted_part(nums, target, mid, right)
    return result


def binary_search(nums: list, target: int, left: int, right: int) -> int:
    """Binary search."""
    # base cases
    if left >= right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid

    # recursion
    if target < nums[mid]:
        return binary_search(nums, target, left, mid)
    if nums[mid] < target:
        return binary_search(nums, target, mid + 1, right)


def broken_search(nums: list, target: int) -> int:
    """Recieves partly sorted array and target for searching in it."""
    return handle_sorted_part(nums, target)


def test():
    """Test is test."""
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 1) == 4


test()
