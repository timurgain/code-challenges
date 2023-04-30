"""Палиндром."""

import re


def read_input() -> tuple:
    words = input().strip().replace(' ', '')
    words = re.sub(r'[^\w\s]', '', words)    
    return list(words.lower())

def func(words):
    for i in range(0, len(words)//2):
        if words[i] != words[len(words)-1-i]:
            return False
    return True

if __name__ == '__main__':
    words = read_input()
    y = func(words)
    print(y)
