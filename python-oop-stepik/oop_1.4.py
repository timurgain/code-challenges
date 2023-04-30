class Translator:
    def __init__(self):
        self.dictionary = {}

    def add(self, eng, rus):
        item = self.dictionary.setdefault(eng, [])
        if rus not in item:
            item.append(rus)

    def remove(self, eng):
        if self.dictionary.get(eng, False):
            del self.dictionary[eng]

    def translate(self, eng):
        return self.dictionary.get(eng)


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')

print(*tr.translate('go'))
