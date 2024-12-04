"""Модуль: guessing_game.

Игра - Числовая угадайка.
"""

from random import randint


def generating_number() -> int:
    return randint(1, 100)


def is_valid(num: int) -> bool:
    if 1 <= num <= 100:
        return True
    else:
        return False


def main() -> None:
    hidden_number = generating_number()
    while True:
        guess = int(input('Введите число от 1 до 100:  '))
        switch = is_valid(guess)
        if not switch:
            print('А может быть все-таки введем целое число от 1 до 100?')
        else:
            if guess < hidden_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif guess > hidden_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


if __name__ == '__main__':
    print('Добро пожаловать в игру числовая угадайка')
    main()
