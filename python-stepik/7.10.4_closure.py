def tagger(s: str) -> str:
    def wrapper() -> str:
        return f'<h1>{s}</h1>'
    return wrapper


if __name__ == '__main__':
    words = input()
    res = tagger(words)
    print(res())