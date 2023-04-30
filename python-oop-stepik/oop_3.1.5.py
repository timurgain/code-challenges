class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id: int
    name: str
    weight: int or float
    price: int or float

    count_items = 0

    def __new__(cls, *args, **kwargs):
        cls.count_items += 1
        return super().__new__(cls)

    def __init__(self, name: str, weight: int, price: int) -> None:
        self.id = self.count_items
        self.name = name
        self.weight = weight
        self.price = price

    def __delattr__(self, name: str) -> None:
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super.__delattr__(self, name)

    def __setattr__(self, name, value) -> None:
        if not isinstance(value, self.__annotations__.get(name)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if self.__annotations__.get(name) in (int, float) and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        super.__setattr__(self, name, value)


if __name__ == '__main__':
    shop = Shop("Балакирев и К")
    book = Product("Python ООП", 100, 1024)
    # book2 = Product("Python ООП", 0, 1024)
    shop.add_product(book)
    shop.add_product(Product("Python", 150, 512))
    shop.remove_product(book)
    for p in shop.goods:
        # print(p.__dict__)
        # print(p.__dir__())
        print(f"{p.name}, {p.weight}, {p.price}")
