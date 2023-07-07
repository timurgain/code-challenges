"""Write a function that takes a string as input and checks whether it can be
 a valid palindrome by removing at most one character from it."""

def is_palindrome_slice(s: str) -> bool:
    print(s)
    if len(s) < 1:
        return False

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def could_it_be_palindrome(s: str) -> bool:
    if len(s) < 1:
        return False

    left, right, dismatch = 0, len(s) - 1, 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            dismatch += 1
            if dismatch > 1:
                return False

            if is_palindrome_slice(s[left:right]):
                return True

            if is_palindrome_slice(s[left+1:right+1]):
                return True
    return True


if __name__ == '__main__':
    # s = 'madame'
    s = 'abcdedadedecba'  # abc dedaded (e) cba
    res = could_it_be_palindrome(s)
    print(res)
