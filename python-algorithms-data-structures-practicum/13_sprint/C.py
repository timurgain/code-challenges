"""C. Подпоследовательность."""


def read_input() -> tuple:
    return input(), input()


def subsequence(substring: str, sequence: str) -> bool:
    if len(substring) > len(sequence):
        return False
    if len(substring) == 0:
        return True
    match = 0
    for i in range(0, len(sequence)):
        if substring[match] == sequence[i]:
            match += 1
            if match == len(substring):
                return True
    return False


if __name__ == '__main__':
    sub, seq = read_input()
    print(subsequence(sub, seq))
