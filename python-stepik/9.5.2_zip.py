from typing import Iterable

def multiply_collections(a: Iterable[int], b: Iterable[int]) -> Iterable:
    """Multiplies items in two collections."""
    return map(lambda x: x[0] * x[1], [*zip(a, b)])


if __name__ == '__main__' :
    a = map(int, input().split(' '))
    b = map(int, input().split(' '))
    res = multiply_collections(a, b)
    print(next(res), next(res), next(res))
