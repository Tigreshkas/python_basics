# Написать декоратор для логирования типов позиционных аргументов функции.
from functools import wraps


def val_checker(fun_lam):  # передаем аргумент декоратора (в данном случае лямбда-функцию)
    def _logger(callback):  # передаем функцию, к которой применяем декоратор
        @wraps(callback)  # декорируем функцию wrapper
        def wrapper(*args):  # передаем аргументы, из функции, к которой применяем декоратор
            if fun_lam(*args):  # проверяем соответствие аргумента лямбда-функции
                result = callback(*args)  # если всё хорошо, вызываем функцию для введенного аргумента
                return result
            else:  # если не соответствует, выдаем ошибку
                raise ValueError(f'wrong val {args[0]}')
        return wrapper
    return _logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Calculates box area"""
    return x ** 3


a = calc_cube(5)
print(a)
help(calc_cube)
