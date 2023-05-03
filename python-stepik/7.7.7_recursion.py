from typing import Optional


def get_line_list(source: list, result: Optional[list] = None) -> list:
    """Makes a line list from a nested list."""
    result = [] if result is None else result
    if type(source) != list:
        result.append(source)
    else:
        for item in source:
            get_line_list(item, result)
    return result


if __name__ == '__main__':
    d = [1, 2, [True, False], ["Спб", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
    l = get_line_list(d)
    print(d)
    print(l)