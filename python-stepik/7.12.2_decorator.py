from functools import wraps

# plain decorator
def adder(func):
    """Adds 5 to a func result. Manual override wrapper's__name__, __doc__"""
    def wrapper(s: str, *ags, **kwargs):
        """wrapper docstring."""
        return func(s) + 5
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@adder
def sum_str(s: str) -> int:
    """Takes str, converts to list[int], returns sum of int."""
    gen_lst = map(int, s.split(' '))
    return sum(gen_lst)


# decorator with params
def adder_params(plus: int = 5):
    """adder_params."""
    def adder(func):
        """Adds 'plus' to a func result."""
        @wraps(func)
        def wrapper(s: str, *args, **kwargs):
            """wrapper docstring."""
            return func(s) + plus
        return wrapper
    return adder

@adder_params(plus=10)
def another_sum_str(s: str) -> int:
    """Takes str, converts to list[int], returns sum of int."""
    gen_lst = map(int, s.split(' '))
    return sum(gen_lst)


if __name__ == '__main__':
    s = input()

    print(sum_str.__name__, sum_str.__doc__)
    print(sum_str(s))

    print(another_sum_str.__name__, another_sum_str.__doc__)
    print(another_sum_str(s))
