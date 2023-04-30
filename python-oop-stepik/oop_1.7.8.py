from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        is_len_ok = 3 <= len(name) <= 50
        is_chars_ok = not any(char not in cls.CHARS_CORRECT for char in name)
        if any((not is_len_ok, not is_chars_ok)):
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name, self.size = name, size

    def get_html(self):
        return (f"<p class='login'>{self.name}:"
                f" <input type='text' size={self.size} />")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        is_len_ok = 3 <= len(name) <= 50
        is_chars_ok = not any(char not in cls.CHARS_CORRECT for char in name)
        if any((not is_len_ok, not is_chars_ok)):
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name, self.size = name, size

    def get_html(self):
        return (f"<p class='password'>{self.name}:"
                f" <input type='text' size={self.size} />")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
