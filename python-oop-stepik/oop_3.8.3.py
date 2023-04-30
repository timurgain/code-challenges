class Record:
    def __init__(self, **kwargs):
        self._attr_list = []
        for key, value in kwargs.items():
            self.__dict__[key] = value
            self._attr_list.append(key)

    def __getitem__(self, index):
        if not isinstance(index, int) or index >= len(self._attr_list):
            raise IndexError('неверный индекс поля')
        key = self._attr_list[index]
        return self.__dict__[key]

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index > len(self._attr_list):
            raise IndexError('неверный индекс поля')
        if index == len(self._attr_list):
            self.__dict__[index] = value
        key = self._attr_list[index]
        self.__dict__[key] = value


if __name__ == '__main__':
    r = Record(pk=1, title='Python ООП', author='Балакирев')

    r[0] = 2 # доступ к полю pk
    r[1] = 'Супер курс по ООП' # доступ к полю title
    r[2] = 'Балакирев С.М.' # доступ к полю author
    print(r[1]) # Супер курс по ООП
    r[3]  # генерируется исключение IndexError
