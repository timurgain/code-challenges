"""
1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник."""


# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, *sides):
        self.sides = sides

    def is_triangle(self):
        if any(type(sd) not in (int, float) or sd <= 0 for sd in self.sides):
            return 1
        return 2 if max(self.sides) >= sum(self.sides) - max(self.sides) else 3


a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
