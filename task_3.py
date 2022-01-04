# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def class_name(name_tutors, klass_number):  # Создаем генератор (т.к. используем вместо return yield)
    """Generator of tuples of the form (<tutor>, <klass>)"""
    for name, klass in zip(name_tutors, klass_number):  # склеиваем элементы списков через zip, пока значения есть
        # в каждом списке
        result = (name, klass)  # присваиваем переменной кортеж определенного вида
        yield f'{result}\n'  # выводим переменную (каждый раз с новой строки)
    if len(name_tutors) > len(klass_number):  # если длина списка с именами длинее списка классов, то
        for name in name_tutors[len(klass_number) - len(name_tutors):]:  # для имён, входящих в срез
            # от неиспользованных элементов до конца списка
            result = (name, 'None')  # присваиваем переменной имя и вместо класса "None"
            yield f'{result}\n'
    else:  # если длина списка с классами длинее списка имён, то
        for klass in klass_number[len(name_tutors) - len(klass_number):]:  # для классов, входящих в срез
            # от неиспользованных элементов до конца списка
            result = ('None', klass)  # присваиваем переменной класс и вместо имени "None"
            yield f'{result}\n'


print(*class_name(tutors, klasses))  # выводим результат выполнения генератора, изначально вытянув из списков все эл-ты
