"""B. Калькулятор. ID принятого решения в Яндекс.Контест: 66576003."""
import operator


OPERATIONS = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'floordiv',  # //
}


class ErrorStackLength(Exception):
    """Stack length error."""
    pass


class Stack():
    """Stack data structure."""
    def __init__(self):
        self.stack = []
        self.length = 0

    def pop(self):
        """Get and delete the last object in the Stack."""
        if self.length < 1:
            raise ErrorStackLength
        self.length -= 1
        return self.stack.pop()

    def put(self, value):
        """Put the object in the end of Stack."""
        self.stack.append(value)
        self.length += 1

    def __str__(self):
        return f"This Stack instance contains {self.length} objects."


def read_input() -> list:
    """Reads input from a terminal or file."""
    return input().strip().split()


def calculator_for_reverse_notation(values: list) -> int:
    """Solves a sequence with reverse polish notation."""
    numbers = Stack()
    for value in values:
        if value not in OPERATIONS.keys():
            numbers.put(int(value))
        else:
            args = numbers.pop(), numbers.pop()
            numbers.put(getattr(operator, OPERATIONS[value])(args[1], args[0]))
    return numbers.pop()


if __name__ == '__main__':
    values = read_input()
    print(calculator_for_reverse_notation(values))
