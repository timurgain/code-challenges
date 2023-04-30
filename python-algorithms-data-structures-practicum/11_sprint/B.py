def read_input() -> tuple:
    a, x, b = list(map(int, input().strip().split()))
    return a, x, b

def func(a, x, b):
    if a%2 == 0 and x%2 == 0 and b%2 == 0:
        return 'WIN'
    if a%2 == 1 and x%2 == 1 and b%2 == 1:
        return 'WIN'
    else:
        return 'FAil'
    
    return y

a, x, b = read_input()
print(func(a, x, b))
