def counter_add(n: int) -> int:
    def adder(j: int) -> int:
        return j + n
    return adder


if __name__ == '__main__':
    cnt = counter_add(2)
    k = int(input())
    print(cnt(k))
