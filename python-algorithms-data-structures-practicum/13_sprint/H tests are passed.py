"""H. Большое число."""
import functools


def read_input():
    length = int(input())
    numbers = input().split(' ')
    return length, numbers


def compare(a, b):
    if (a[0] * 10 ** len(b[1]) + b[0]) > (b[0] * 10 ** len(a[1]) + a[0]):
        return -1
    else:
        return 1


if __name__ == '__main__':
    length, numbers = read_input()
    array = [tuple([int(num), num]) for num in numbers]
    array.sort(key=functools.cmp_to_key(compare))
    print(''.join([num[1] for num in array]), end='')
