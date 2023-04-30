"""J. Пузырёк. Bubble sort."""


def read_input():
    length = int(input())
    array = list(map(int, input().strip().split()))
    return length, array


def bubble_sort(array, length) -> list:
    shift = True
    even_once_shift = False
    while shift:
        shift = False
        for i in range(0, length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                shift = True
                even_once_shift = True
        if shift:
            print(' '.join(map(str, array)))
    if not even_once_shift:
        print(' '.join(map(str, array)))


if __name__ == '__main__':
    length, array = read_input()
    bubble_sort(array, length)
