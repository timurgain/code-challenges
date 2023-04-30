import random


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwds):
        random_length = random.randint(self.min_length, self.max_length)
        pass_list = random.choices(self.psw_chars, k=random_length)
        return ''.join(pass_list)


if __name__ == '__main__':
    min_length = 5
    max_length = 20
    psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

    rnd = RandomPassword(psw_chars, min_length, max_length)

    lst_pass = [rnd() for _ in range(3)]
