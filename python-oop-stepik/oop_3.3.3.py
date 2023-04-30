import sys


class Book:
    def __init__(self, *args):
        self.title, self.author, self.pages = args

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, sys.stdin.readlines()))


book = Book(*lst_in)

print(book)
