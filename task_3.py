# Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

class CheckingForNumbers(Exception):
    pass


list_numbers = []
number = 0
while number != 'stop':
    number = input('Введите число или команду "stop": ')
    if number == 'stop':
        print(list_numbers)
        break
    else:
        try:
            if not number.isdigit():
                raise CheckingForNumbers('Должны быть только числа!')
        except CheckingForNumbers as err:
            print(err)
        else:
            list_numbers.append(int(number))
