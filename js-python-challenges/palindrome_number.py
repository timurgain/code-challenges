"""Given an integer x, return true if x is a palindrome, and false otherwise"""

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x < 10:
        return True
    if x < 100:
        return x//10 == x%10

    arr = []
    while x > 0:
        arr.append(x%10)
        x = x//10

    for i in range(len(arr)//2):
        if arr[i] != arr[-1-i]:
            return False

    return True


if __name__ == '__main__':
    print(isPalindrome(123321))
