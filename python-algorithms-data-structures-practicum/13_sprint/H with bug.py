"""H. Большое число. Тут есть неотловленный баг."""
from typing import List


def read_input():
    length = int(input())
    numbers = list(input().strip().split())
    return length, numbers


def number_streght(number: str, char_idx: int) -> int:
    return int(number[char_idx]) if (len(number) >= char_idx + 1) else 0


# 7
# 9 6 66 69 6 64 79

#
# 882825823810
# 825
def key_sort(numbers: List[str], length: int) -> List[str]:
    shift = True
    while shift:
        shift = False

        # iterate over the range by array length, except the last number
        for num_idx in range(0, length-1):

            # print(f"{numbers[num_idx]} and {numbers[num_idx+1]}", end=' -> ')

            this_num_length = len(numbers[num_idx])
            next_num_length = len(numbers[num_idx+1])

            # iterate over the range by longest number length
            for char_idx in range(0, min(this_num_length, next_num_length)):
                this_num_char = number_streght(numbers[num_idx], char_idx)
                next_num_char = number_streght(numbers[num_idx+1], char_idx)

                # next_num_char is stronger
                if this_num_char < next_num_char:
                    numbers[num_idx], numbers[num_idx+1] = numbers[num_idx+1], numbers[num_idx]
                    shift = True
                    break
                # next_num_char is weaker
                if this_num_char > next_num_char:
                    break

                # next number is shorter and extra chars are weaker
                if (this_num_length > next_num_length
                   and char_idx == next_num_length - 1  # last char for the next number
                   and number_streght(numbers[num_idx], char_idx) > number_streght(numbers[num_idx], char_idx + 1)):
                    numbers[num_idx], numbers[num_idx+1] = numbers[num_idx+1], numbers[num_idx]
                    shift = True
                    break

                # this number is shorter and extra chars are stronger
                if (this_num_length < next_num_length
                   and char_idx == this_num_length - 1  # last char for the next number
                   and number_streght(numbers[num_idx+1], char_idx) < number_streght(numbers[num_idx+1], char_idx + 1)):
                    numbers[num_idx], numbers[num_idx+1] = numbers[num_idx+1], numbers[num_idx]
                    shift = True
                    break

            # print(f"{numbers[num_idx]} and {numbers[num_idx+1]}")
        # print(''.join(numbers))
    return numbers


if __name__ == '__main__':
    length, numbers = read_input()
    print(''.join(key_sort(numbers, length)))
