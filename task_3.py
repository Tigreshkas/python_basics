# Задание 3. Написать декоратор для логирования типов позиционных аргументов функции.
from functools import wraps


def type_logger(callback):  # передаем функцию в декоратор
    @wraps(callback)  # маскируем работу декоратора
    def wrapper(*args):  # передаем аргументы в декоратор
        return f'{callback.__name__}({args[0]}: {type(args[0])})'  # <имя функции>(<аргумент>: <тип аргумента>)
    return wrapper


@type_logger
def calc_cube(x):
    """Calculates box area"""
    return x ** 3


a = [5, 7, 9]
for num in a:
    print(calc_cube(num))
help(calc_cube)
