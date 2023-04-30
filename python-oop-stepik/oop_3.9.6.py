class Person:
    fio: str
    job: str
    old: int
    salary: int or float
    year_job: int

    def __init__(self, *args):
        i = 0
        for key in Person.__annotations__.keys():
            setattr(self, key, args[i])
            i += 1
        self.__keys = list(Person.__annotations__.keys())

    def __check_index(func):
        def wrapper(self, *args, **kwargs):
            try:
                index = args[0]
                assert index in range(0, 5)  # int and from 0 to 4
                return func(self, *args, **kwargs)
            except Exception:
                raise IndexError('неверный индекс')
        return wrapper

    @__check_index
    def __getitem__(self, index):
        return getattr(self, self.__keys[index])

    @__check_index
    def __setitem__(self, index, value):
        setattr(self, self.__keys[index], value)

    def __iter__(self):
        self.__current = -1
        return self

    def __next__(self):
        self.__current += 1
        if self.__current < len(self.__keys):
            attr_name = self.__keys[self.__current]
            return self.__dict__[attr_name]
        raise StopIteration


if __name__ == '__main__':
    pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
    pers[1] = 'рабочий'

    print(pers[1])

    for attr in pers:
        print(attr)

    print(pers[1])

    for attr in pers:
        print(attr)
