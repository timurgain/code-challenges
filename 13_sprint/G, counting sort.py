"""G. Гардероб / Wardrobe, counting sort."""


TYPES = 3


def read_input():
    amount = int(input())
    dresses = list(map(int, list(input().strip().split())))
    return amount, dresses


def counting_sort(clothes):
    items = [0] * TYPES
    for dress in dresses:
        items[dress] += 1

    for i in range(0, len(items)):
        while items[i] > 0:
            print(i, end=' ')
            items[i] -= 1


if __name__ == '__main__':
    amount, dresses = read_input()
    counting_sort(dresses)
