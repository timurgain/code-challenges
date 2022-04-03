"""A. Ближайший ноль. ID принятого решения в Яндекс.Контест: 66012582"""


def read_input() -> tuple:
    """Read input from a terminal or file."""
    length = int(input())
    houses = list(input().strip().split())
    return length, houses


def get_distances_to_zero(length, houses):
    """Returns the distances to adjacent zeros in a list."""
    result = ['0']*length
    zero_indexes = [i for i in range(0, length) if houses[i] == '0']
    if len(zero_indexes) == length:
        return ' '.join(result)

    for zer in range(len(zero_indexes)):

        # the first zero place
        if zer == 0:
            for res in range(0, zero_indexes[zer]):
                result[res] = str(zero_indexes[zer] - res)

        # an interval between two zeros
        if zer != len(zero_indexes) - 1:
            for res in range(zero_indexes[zer], zero_indexes[zer + 1] - 1):
                left = res - zero_indexes[zer] + 1
                right = zero_indexes[zer + 1] - res - 1
                result[res+1] = str(left if left <= right else right)

        # the last zero place
        if zer == len(zero_indexes) - 1:
            for res in range(zero_indexes[zer] + 1, length):
                result[res] = str(res - zero_indexes[zer])

    return ' '.join(result)


if __name__ == '__main__':
    length, houses = read_input()
    print(get_distances_to_zero(length, houses))
