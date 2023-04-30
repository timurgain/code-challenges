def read_input() -> tuple:
    a, x, b, c = list(map(int, input().strip().split()))
    return a, x, b, c

def func(a, x, b, c):
    y = x*(a*x + b) + c
    return y

a, x, b, c = read_input()
y = func(a, x, b, c)
print(y)
