def prime_finder(n):
    """Prime Number Finder."""
    result = []
    if n <= 1:
        return result

    for num in range(2, n+1):
        for d in range(2, (num//2)+2):
            if num % d == 0 and num != d:
                break
            if d == (num//2)+1:
                result.append(num)

    return result


print(prime_finder(49))
