def counter_add(value: int) -> int:
    def adder() -> int:
        return value + 5
    return adder()


if __name__ == '__main__':
    k = int(input())
    cnt = counter_add(k)
    print(cnt)
