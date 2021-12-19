# Задание на список кубов нечётных чисел

number_cube = []
for i in range(1, 1001, 2):
    number_cube.append(i ** 3)
# print(number_cube)     # вывод кубов нечетных чисел от 1 до 1000
#copy_cube = number_cube.copy()
sum_all_numbers = 0
sum_all_numbers2 = 0

for i in range(0, len(number_cube)):
    copy_cube = number_cube.copy()
    sum_number = 0
    while copy_cube[i] > 0:  # находим сумму цифр каждого числа в копии списка
        sum_number += copy_cube[i] % 10  # тут работаем с копией списка, потому что
        copy_cube[i] = copy_cube[i] // 10  # при выполнении цикла список обнуляется
    if sum_number % 7 == 0:  # находим сумму тех чисел из копии списка, сумма цифр которых делится на 7
        sum_all_numbers += number_cube[i]
    number_cube[i] = number_cube[i] + 17    # прибавляем к каждому числу в основном списке 17
                                            # написано именно тут, чтобы не создавать новый список
print(f'Вариант а: сумма всех чисел, сумма всех цифр которых делится на 7 = {sum_all_numbers}')
#print(number_cube)     # вывод всех чисел списка + 17
for i in range(0, len(number_cube)):
    copy_cube2 = number_cube.copy()
    sum_number2 = 0
    while copy_cube2[i] > 0:  # находим сумму цифр каждого числа в списке
        sum_number2 += copy_cube2[i] % 10
        copy_cube2[i] = copy_cube2[i] // 10
    if sum_number2 % 7 == 0:  # находим сумму тех чисел из списка, сумма цифр которых делится на 7
        sum_all_numbers2 += number_cube[i]
print(f'Вариант b: сумма всех чисел (+17), сумма всех цифр которых делится на 7 = {sum_all_numbers2}')
