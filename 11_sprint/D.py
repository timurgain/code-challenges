def read_input() -> tuple:
    total_days = int(input())
    temperatures = (list(map(int, input().strip().split())))
    return total_days, temperatures

def func(total_days, temperatures):
    if total_days == 1:
        return 1
    counter = 0 
    if total_days == 2:
        if temperatures[0] != temperatures[1]:
            return 1
    if total_days >= 3:
        if temperatures[0] > temperatures[1]:
            counter += 1
        for i in range(1, total_days-1):        
            if (temperatures[i-1] < temperatures[i]
            and temperatures[i] > temperatures[i+1]):
                counter += 1
        for end in range(total_days-1, total_days):
            if temperatures[end-1] < temperatures[end]:
                counter += 1
    
    return counter

if __name__ == '__main__':
    total_days, temperatures = read_input()
    y = func(total_days, temperatures)
    print(y)
