def read_input() -> tuple:
    length = int(input())
    words = input().strip().split()
    return length, words

def func(length, words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return f"{longest}\n{len(longest)}"    

if __name__ == '__main__':
    length, words = read_input()
    y = func(length, words)
    print(y)
