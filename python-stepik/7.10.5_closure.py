from typing import Callable

def outer(tp: str) -> Callable:
    """Reads the type, then the data, then converts the data into the type."""
    def inner(data: str):
        res_gen = map(int, data.split(' '))
        return list(res_gen) if tp == 'list' else tuple(res_gen)
    return inner

if __name__ == '__main__':
    tp = input()
    data = input()
    lst = outer(tp)
    print(lst(data))
