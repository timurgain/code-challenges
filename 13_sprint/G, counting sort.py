"""G. Гардероб / Wardrobe, counting sort."""


ITEMS = {
    '0': 0,
    '1': 0,
    '2': 0,
}


def read_input_and_counting_sort():
    amount = int(input())
    if amount > 0:
        for item in input().split(' '):
            ITEMS[item] += 1
        for item, count in ITEMS.items():
            print((item + ' ') * count, end='')


if __name__ == '__main__':
    read_input_and_counting_sort()
