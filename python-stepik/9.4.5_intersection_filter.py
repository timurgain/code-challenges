def input_str_to_int_list() -> list[int]:
    """Works with input, returns a list of int."""
    return list(map(int, input().split(' ')))

def get_sorted_intersection(a: list[int], b: list[int]) -> list[int]:
    """Takes collections, returns a sorted list of intersection of int."""
    intersection = set(a).intersection(b)
    return sorted(list(intersection))

def is_even_number(x: int) -> bool:
    """Checks if number is even."""
    return x % 2 == 0

if __name__ == '__main__':
    coins_1 = input_str_to_int_list()
    coins_2 = input_str_to_int_list()
    lst = get_sorted_intersection(coins_1, coins_2)
    lst = filter(is_even_number, lst)
    print(*lst)
