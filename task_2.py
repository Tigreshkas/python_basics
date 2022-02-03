# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.

class DivZero(Exception):
    pass


number_1 = input('Введите делимое: ')
number_2 = input('Введите делитель: ')
try:
    if number_2 == 0:
        raise DivZero('Делить на 0 нельзя!')
    result = int(number_1) / int(number_2)
except (ValueError, DivZero) as err:
    print(err)
else:
    print(f'Частное = {result:.2f}')
