"""Ограниченная очередь."""


def read_input():
    commands_size = int(input())
    queue_size = int(input())
    commands = []
    for command in range(0, commands_size):
        command = input().strip().split()
        commands.append(command)
    return queue_size, commands


class MyQueueSized():
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, value):
        if self.size == self.max_size:
            return print('error')
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop(self):
        if self.size == 0:
            return print(None)
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return print(value)

    def peek(self):
        print(self.queue[self.head])

    def size(self):
        self.size


if __name__ == '__main__':
    queue_size, commands = read_input()
    my_queue = MyQueueSized(queue_size)
    for command in commands:
        if command[0] == 'peek':
            my_queue.peek()
        if command[0] == 'push':
            my_queue.push(int(command[1]))
        if command[0] == 'pop':
            my_queue.pop()
        if command[0] == 'size':
            print(my_queue.size)
