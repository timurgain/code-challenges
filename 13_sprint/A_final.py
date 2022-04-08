"""A. Search in a broken rounded sorted array."""


def pivot_index(nums: list):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    mid = len(nums) // 2

    # если кусок отсортирован, тогда запустить бинарный поиск в этом куске
    last = len(nums) - 1
    if nums[mid] < nums[last]:
        bynary_search()
    elif nums[0] < nums[mid]:
        bynary_search()

    else:
        pivot_index()


def bynary_search(nums: list):
    if len(nums) == 0:
        return -1
    mid = len(nums) // 2
    if nums[mid] == target:
        return mid

    elif nums[mid] > target:
        return broken_search(nums[:mid], target)
    elif nums[mid] < target:
        return broken_search(nums[mid:], target)


def broken_search(nums: list, target: int) -> int:
    pass


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


test()
