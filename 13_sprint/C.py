"""C. Подпоследовательность."""


def read_input():
    return input(), input()


def subsequence(sub: str, seq: str) -> bool:
    if len(sub) > len(seq):
        return False
    if len(sub) == 0:
        return True
    seq = sorted(seq)
    indexes_found_in_seq = []
    result = [False] * len(sub)
    for char in sub:
        index_found, present = binary_search(seq, char, left=0, right=len(seq))
        if present and (index_found not in indexes_found_in_seq):
            result[sub.index(char)] = True
            indexes_found_in_seq.append(index_found)
    return True if False not in result else False


def binary_search(seq, char, left, right) -> tuple:
    if left >= right:
        return -1, False
    mid = (left + right) // 2
    if seq[mid] == char:
        return mid, True
    elif seq[mid] < char:
        return binary_search(seq, char, mid+1, right)
    elif seq[mid] > char:
        return binary_search(seq, char, left, mid)


if __name__ == '__main__':
    sub, seq = read_input()
    print(subsequence(sub, seq))
