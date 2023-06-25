def is_palindrome(s: str) -> bool:
    """Takes a string and determines whether or not it is a palindrome."""
    if len(s) < 1:
        return False
    for i in range(len(s)):
        if i < abs(-1-i):
            one = s[i]
            two = s[-1-i]
            if one != two:
                return False
    return True

if __name__ == '__main__':
    s = 'moomk'
    print(is_palindrome(s))
