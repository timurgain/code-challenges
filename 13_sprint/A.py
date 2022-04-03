"""A. Генератор скобок."""


def read_input() -> tuple:
    length = int(input())
    return length


def generator(length, left=0, right=0, result='', ):
    if length == left and length == right:
        print(result)
    else:
        # на прямом ходе
        if length > left:
            generator(length, left + 1, right, result + '(')
        # на обратном ходу правые скобки контролим количеством левых
        if left > right:
            generator(length, left, right + 1, result + ')')


if __name__ == '__main__':
    length = read_input()
    generator(length)
