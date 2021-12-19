# Склонение слова "процент"

number_list = range(1, 101)

for i in number_list:
    if i == 11 or i == 12 or i == 13 or i == 14:
        print(f'{i} процентов')
    elif i % 10 == 1:
        print(f'{i} процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')