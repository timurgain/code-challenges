"""B. Эффективная быстрая сортировка / Efficient quicksort
ID принятого решения в Яндекс.Контест: 67126472."""


def read_input():
    """Reads an input from a terminal or file."""
    n = int(input())
    rows = 0
    members = []
    while rows < n:
        user, solved, errors = input().split()
        members.append(list((user, int(solved), int(errors))))
        rows += 1
    return members


def output(members: list) -> str:
    """Outputs a result into a console."""
    for i in range(len(members)-1, -1, -1):
        print(members[i][0])


def low_lt_high(low: list, high: list) -> bool:
    """Compares two members, if low < high returns True."""
    if low[1] == high[1]:
        return low[0] > high[0] if low[2] == high[2] else low[2] > high[2]
    return low[1] < high[1]


def quick_sort(members: list, base_left: int = None, base_right: int = None):
    """in-place quick sort, memory consumption is O(1), CPU time is O(n log n).
    """
    base_left = 0 if base_left is None else base_left
    base_right = len(members) - 1 if base_right is None else base_right

    # base case
    if base_left >= base_right:
        return members

    # pivot
    mid = (base_left + base_right) // 2
    pivot = members[mid]

    # sorting
    left, right = base_left, base_right
    while left <= right:
        while low_lt_high(members[left], pivot):
            left += 1
        while low_lt_high(pivot, members[right]):
            right -= 1
        if left <= right:
            members[left], members[right] = members[right], members[left]
            left, right = left + 1, right - 1

    # recursions
    quick_sort(members, base_left, right)
    quick_sort(members, left, base_right)


if __name__ == '__main__':
    members = read_input()
    quick_sort(members)
    output(members)
