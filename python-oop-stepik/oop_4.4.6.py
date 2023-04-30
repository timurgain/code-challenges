class Animal:
    def __init__(self, name, kind, old):
        self.__name, self.__kind, self.__old = name, kind, old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    old = property()

    @old.getter
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


if __name__ == '__main__':
    a = Animal('Васька', 'дворовый кот', 5)
    b = Animal('Рекс', 'немецкая овчарка', 8)
    c = Animal('Кеша', 'попугай', 3)

    animals = [a, b, c]
    print(l)
