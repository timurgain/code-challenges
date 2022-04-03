"""A. Дек, кольцевой буфер. ID принятого решения в Яндекс.Контест: 66574152."""
from typing import Optional


class SizeError(Exception):
    """Deque size error."""
    pass


class DequeSized():
    """Decue data structure with ring buffer."""

    def __init__(self, max_size):
        self.max_size = max_size
        self.deque = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size == self.max_size:
            raise SizeError
        self.tail = (self.head + self.size) % self.max_size
        self.deque[self.tail] = value
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            raise SizeError
        self.head = (self.head - 1) % self.max_size
        self.deque[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise SizeError
        value = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return print(value)

    def pop_back(self):
        if self.size == 0:
            raise SizeError
        self.tail = (self.head + self.size - 1) % self.max_size
        value = self.deque[self.tail]
        self.deque[self.tail] = None
        self.size -= 1
        return print(value)

    def __str__(self):
        return f"This DequeSized instance contains {self.size} objects."


def read_input():
    """Reads input from a terminal or file."""
    commands_size = int(input())
    deque_size = int(input())
    commands = []
    for command in range(0, commands_size):
        command = input().strip().split()
        commands.append(command)
    return commands, deque_size


def performer(deque: DequeSized, commands: list) -> Optional[str]:
    """Performs commands over the DequeSized instance."""
    for command in commands:
        try:
            if len(command) > 1:
                getattr(deque, command[0])(command[1])
                continue
            getattr(deque, command[0])()
        except SizeError:
            print('error')


if __name__ == '__main__':
    commands, deque_size = read_input()
    my_deque = DequeSized(deque_size)
    performer(my_deque, commands)
