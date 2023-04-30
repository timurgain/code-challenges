def read_input():
    return list(input())


def func(brackets):
    if brackets == '':
        return True
    if len(brackets) % 2 != 0:
        return False

    stack = []
    for b in brackets:
        if b in ')]}' and len(stack) == 0:
            return False
        if b in '([{':
            stack.append(b)
        if b in ')]}':
            if b == ')':
                bdel = stack.pop()
                if bdel != '(':
                    return False
            if b == ']':
                bdel = stack.pop()
                if bdel != '[':
                    return False
            if b == '}':
                bdel = stack.pop()
                if bdel != '{':
                    return False
    return True


if __name__ == '__main__':
    brackets = read_input()
    print(func(brackets))
