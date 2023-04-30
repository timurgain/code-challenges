class Rect:
    def __init__(self, *args):
        self.x, self.y, self.width, self.height = args

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.width, self.height))


if __name__ == '__main__':

    r1 = Rect(10, 5, 100, 50)
    r2 = Rect(-10, 4, 100, 50)

    h1, h2 = hash(r1), hash(r2)   # h1 == h2
    print(hash(r1), hash(r2))
