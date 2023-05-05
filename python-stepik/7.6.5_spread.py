def get_gap() -> list:
    return [*map(int, input().split(' '))]

def fill_gap(gap: list) -> list:
    lst = [*range(*gap, 1), gap[1]]
    return ' '.join(map(str, lst))

if __name__ == '__main__':
    gap = get_gap()
    sequence = fill_gap(gap)
    print(sequence)
