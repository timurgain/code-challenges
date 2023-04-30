class WindowDlg:
    def __init__(self, title: str, width: int, height: int):
        # initailization of attributes
        self.__title, self.__width, self.__height = title, None, None
        # validate values, here width and height are already objs of @property
        self.width = width
        self.height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    def _check_size_and_render(func):
        MIN = 0
        MAX = 10000

        def wrapper(self, size):
            if type(size) is int and (MIN <= size <= MAX):
                func(self, size)
                if all(attr is not None for attr in self.__dict__.values()):
                    self.show()
            else:
                raise ValueError('Wrong size')
        return wrapper

    @property
    def width(self):
        return self.__width

    @width.setter
    @_check_size_and_render
    def width(self, width: int):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    @_check_size_and_render
    def height(self, height: int):
        self.__height = height


win = WindowDlg('Окно', 120, 130)
win.height = 30
win.width = 40
