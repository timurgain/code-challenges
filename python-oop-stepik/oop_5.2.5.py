try:
    a, b = input().split()
    res = int(a) + int(b)
except ValueError:
    try:
        res = float(a) + float(b)
    except ValueError:
        res = str(a) + str(b)
finally:
    print(res)
