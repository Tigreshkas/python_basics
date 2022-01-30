# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def expenses(self):  # абстрактный метод
        pass

    def __add__(self, other):
        return self.expenses() + other.expenses()


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'Для пошива пальто {self.size} размера потребуется {self.expenses}м ткани.'

    @property
    def expenses(self):
        return round((self.size/6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height/100

    def __str__(self):
        return f'Для пошива костюма на рост {self.height}м потребуется {self.expenses}м ткани.'

    @property
    def expenses(self):
        return round((2 * self.height + 0.3), 2)


clothes_1 = Coat(46)
clothes_2 = Suit(180)
print(clothes_1)
print(clothes_2)
result = clothes_1.expenses + clothes_2.expenses
print(f'Для пошива всего заказа потребуется {result}м ткани.')
