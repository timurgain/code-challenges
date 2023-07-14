"""Write an algorithm to determine if a number is a happy number.

We use the following process to check if a given number is a happy number:
    - Starting with the given number n, replace the number with the sum of the squares of its digits.
    - Repeat the process until:
        The number equals 1, which will depict that the given number is a happy number.
        It enters a cycle, which will depict that the given number n is not a happy number.

Return TRUE if n is a happy number, and FALSE if not."""


def sum_squared_digits(n: int) -> int:
    res = 0
    while n > 0:
        res += pow(n % 10, 2)
        n //= 10
    return res

def is_happy_number(n: int) -> bool:
    slow = n
    fast = sum_squared_digits(slow)
    print(slow, '<>', fast, 'or == 1')
    while fast != 1 and fast != slow:
        slow = sum_squared_digits(slow)
        fast = sum_squared_digits(sum_squared_digits(fast))
        print(slow, '<>', fast, 'or == 1')
    if fast == 1:
        return True
    return False


if __name__ == "__main__":
    n = 14
    res = is_happy_number(n)
    print(res)
