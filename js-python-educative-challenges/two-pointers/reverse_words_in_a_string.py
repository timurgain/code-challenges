"""Given a sentence, reverse the order of its words without affecting the order
 of letters within a given word."""

import re

def reverse_words(string: str) -> str:
    s = re.sub(' +', ' ', string[::-1].strip())
    first = 0
    second = 0

    while first < len(s):
        while second < len(s) and s[second] != ' ':
            second += 1

        s = f"{s[:first]}{s[first:second][::-1]}{s[second:]}"
        first = second + 1
        second += 1
    return s

if __name__ == '__main__':
    s = "You   are amazing  " * 10
    print(reverse_words(s))
