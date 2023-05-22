def basic_templates(cmd: int | float | str | bool):
    """Basic demo of match/case statement."""
    match cmd:
        case 657:
            print('Number in case')
        case 'smth' as com:
            print(com)
        case str() as command if len(command) > 5 and command[0] == 't':
            print(f"string command, starts from f")
        case bool():
            print(f"boolean command")
        case int() | float() as command:
            print(command)
        case _:
            print('Default case')


def collections_templates(cmd: list | tuple | dict):
    """Collections demo of match/case statement."""
    match cmd:
        case list() as book:
            print(f'BookList {book[0]} - {book[1]}')
        case tuple() as book:
            print(f'BookTuple {book[0]} - {book[1]}')
        case dict() as book:
            print(f"BookDict {book.get('name')} - {book.get('author')}")
        case _:
            print('Unknown data format')


def collections_templates_unpacked(cmd: list | tuple):
    """Collections demo of match/case statement."""
    match cmd:
        case (name, author) | (_, name, author, *_):
            print('Two similar pattern in one')
        case (name, author, *rest) if len(cmd) > 5:
            print(f'Unpacked BookList with rest case: {name} - {author}')
        case (str() as name, str() as author, int() | float() as yeah, *rest) if len(cmd) > 5:
            print(f'Unpacked BookList with rest case and validation: {name} - {author}')
        case tuple() as book:
            print(f'BookTuple {book[0]} - {book[1]}')
        case dict() as book:
            print(f"BookDict {book.get('name')} - {book.get('author')}")
        case {'name': name, 'author': author}:
            print(f"BookDict {name} - {author}")
        case _:
            print('Unknown data format')


def dict_set_templates_unpacked(cmd: dict | set):
    match cmd:
        case dict() as book:
            print(f"BookDict {book.get('name')} - {book.get('author')}")
        case {'name': name, 'author': author}:
            print(f"BookDict {name} - {author}")
        case {'access': access, 'info': [_, {'email': email}, _, _]}:
            print(f"json {access} - {email}")
        case _:
            print('Unknown data format')


if __name__ == '__main__':

    # basic types
    basic_templates(cmd=3.4)
    basic_templates(cmd='test string')
    basic_templates(cmd=[3, 5,])

    # collections
    book_t: tuple = ('Atlant shrugged', 'Ayn Rand', 1957, '$20')
    book_l: list = ['Atlant shrugged', 'Ayn Rand', 1957, '$20']
    book_rest: tuple = ('Atlant shrugged', 'Ayn Rand', 1957, '$20', 56, 76, False)

    book_d: dict = {'name': 'Atlant shrugged', 'author': 'Ayn Rand', 'year': 1957, 'price': '$20'}
    book_json: dict = {'id': 3, 'access': True, 'info': ['01.01.1991', {'login': 'qwer', 'email': 'e@e.com'}, False, 7.6]}


    # by type
    collections_templates(book_t)
    collections_templates(book_l)
    collections_templates(book_rest)

    # unpacked
    dict_set_templates_unpacked(book_d)
    dict_set_templates_unpacked(book_json)
