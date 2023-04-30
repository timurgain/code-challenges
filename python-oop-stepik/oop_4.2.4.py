class ListInteger(list):
    def __init__(self, args):
        if all(isinstance(i, int) for i in args) is not True:
            raise TypeError('можно передавать только целочисленные значения')
        super().__init__(args)

    def __setitem__(self, index, value):
        if all(isinstance(_, int) for _ in (index, value)) is not True:
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(index, value)

    def append(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('можно передавать только целочисленные значения')
        super().append(value)


if __name__ == '__main__':
    s = ListInteger((11, 22, 33))
    s[1] = 10
    # s.append(11)
    print(s)
    s[0] = 10.5 # TypeError