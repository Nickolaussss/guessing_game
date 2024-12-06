"""Модуль: guessing_game.

Игра - Числовая угадайка.
"""

from random import randint, choice
from gameparts.texts import final, greeting, congratulations, more, less, prompts


def generating_number() -> int:
    """Генерация случайного целого числа."""
    return randint(1, 100)


def is_valid(num: int) -> bool:
    """Проверяет корректность введенного числа от пользователя"""
    if 1 <= num <= 100:
        return True
    else:
        return False


def main() -> None:
    """Главная функция игры."""
    hidden_number = generating_number()
    while True:
        guess = int(input('Введите число от 1 до 100:  '))
        switch = is_valid(guess)
        if not switch:
            print(choice(prompts))
        else:
            if guess < hidden_number:
                print(choice(less))
            elif guess > hidden_number:
                print(choice(more))
            else:
                print(choice(congratulations))
                break
    print(choice(final))


if __name__ == '__main__':
    print(choice(greeting))
    main()
