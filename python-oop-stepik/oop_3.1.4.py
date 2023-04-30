class Book:
    title: str
    author: str
    pages: int
    year: int

    def __init__(self, title='', author='', pages=0, year=0):
        args = title, author, pages, year
        self.title, self.author, self.pages, self.year = args

    def __setattr__(self, key, value) -> None:
        if not isinstance(value, self.__annotations__.get(key, object)):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
