"""
Given a roman numeral, convert it to an integer.
"""

def roman_to_integer(s: str) -> int:
    """Converts roman numbers to integer."""
    dct = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0
    i = 0
    while i < len(s):
        if i == len(s)-1:
            result += dct[s[i]]
            i += 1
            continue
        if dct[s[i]] < dct[s[i+1]]:
            result += dct[s[i+1]] - dct[s[i]]
            i += 2
        else:
            result += dct[s[i]]
            i += 1

    return result


if __name__ == '__main__':
    res = roman_to_integer("MCMXCIV")  # 1994
    print(res)
