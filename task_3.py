# Реализовать базовый класс Worker (работник).

class Worker:  # родительский класс
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):  # дочерний класс
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):  # функция выводит имя и фамилию
        print(f'{self.name} {self.surname}')

    def get_total_income(self):  # функция выводит доход
        total_income = self._income['wage'] + self._income['bonus']  # ссумируем показатели оклада и премии
        print(f'Income {total_income}$')


staffer_1 = Position('Helen', 'Ponomareva', 'chiev specialist', {'wage': 1000, 'bonus': 300})
# print(vars(staffer_1))
staffer_1.get_full_name()  # вызываем необходимый метод
staffer_1.get_total_income()
