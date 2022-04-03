"""B. Комбинации.
На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв.
Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.
"""

# index in KEYBOARD tuple is equal to button on an simple cellphone
KEYBOARD = (
    '',  # 0 button
    '',  # 1 button
    'abc',  # 2 button
    'def',  # 3 button
    'ghi',  # 4 button
    'jkl',  # 5 button
    'mno',  # 6 button
    'pqrs',  # 7 button
    'tuv',  # 8 button
    'wxyz',  # 9 button
)


def read_input() -> list:
    buttons = list(map(int, list(input())))
    return buttons


def generator(buttons: list) -> list:
    if len(buttons) == 1:  # base case or final of recursion
        return KEYBOARD[buttons[0]]

    result = []

    for i in range(0, len(buttons)):

        button_1 = KEYBOARD[buttons[i]]
        button_2 = generator(buttons[i+1:])  # recursive case and deepening

        for i in range(0, len(button_1)):
            for j in range(0, len(button_2)):
                result.append(button_1[i] + button_2[j])
        return result


if __name__ == '__main__':
    buttons = read_input()
    result = generator(buttons)
    print(' '.join(result))
