def read_input(stack):
    commands_ammount = int(input())
    for i in range(0, commands_ammount):
        command = list(input().strip().split())
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'get_max':
            stack.get_max()


class StackMax():
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        try:
            if self.max_items[-1] <= item:
                self.max_items.append(item)
        except IndexError:
            self.max_items.append(item)

    def pop(self):
        try:
            rm_item = self.items.pop()
            if rm_item == self.max_items[-1]:
                self.max_items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        if len(self.max_items) > 0:
            print(self.max_items[-1])
        else:
            print(None)


if __name__ == '__main__':
    stack = StackMax()
    read_input(stack)
