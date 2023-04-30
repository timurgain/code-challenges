from random import randrange, choice, sample


class Figure:
    """Base figure class."""
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Figure):
    pass


class Rect(Figure):
    pass


class Ellipse(Figure):
    pass


figures = (Line, Rect, Ellipse)


def fill_figures(amount: int, figures: tuple) -> list:
    """Retern filled list with random figures, then reset to 0 Line attrs."""
    elements = []
    for _ in range(amount):
        points = sample(range(50), k=4)
        el = choice(figures)(*points)
        elements.append(el)

    for el in elements:
        if isinstance(el, Line):
            for key, _ in el.__dict__.items():
                setattr(el, key, (0, 0))
    return elements


if __name__ == '__main__':
    elements = fill_figures(217, figures)
