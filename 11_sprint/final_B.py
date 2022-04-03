"""B. Ловкость рук. ID принятого решения в Яндекс.Контест: 66012819"""


def read_input() -> tuple:
    """Read input from a terminal or file."""
    values = []
    fingers = int(input())*2
    row = 1
    while row < 5:
        values += list(input())
        row += 1
    return fingers, values


def count_scores(fingers, values):
    """Returns the number of character counts that match the conditions."""
    scores = ([values.count(value) for value in set(values)
              if value != '.' and values.count(value) <= fingers])
    return len(scores)


if __name__ == '__main__':
    fingers, values = read_input()
    print(count_scores(fingers, values))
