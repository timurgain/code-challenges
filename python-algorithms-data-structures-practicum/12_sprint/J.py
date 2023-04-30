"""Списочная очередь."""


def read_input():
    commands_size = int(input())
    commands = []
    for command in range(0, commands_size):
        command = input().strip().split()
        commands.append(command)
    return commands


class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class MyQueueList():
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 1 if head is not None else 0

    def put(self, value):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next_node = self.node
            self.tail = self.node
        self.size += 1

    def get(self):
        if self.size == 0:
            return print('error')
        print(self.head.value)
        self.head = self.head.next_node
        self.size -= 1

    def size(self):
        self.size


if __name__ == '__main__':
    commands = read_input()
    my_queue = MyQueueList()
    for command in commands:
        if command[0] == 'put':
            my_queue.put(command[1])
        if command[0] == 'get':
            my_queue.get()
        if command[0] == 'size':
            print(my_queue.size)
