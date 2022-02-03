# 4. Начать работу над проектом «Склад оргтехники».
# 5. Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразд. компании.
# 6. Реализовать механизм валидации вводимых пользователем данных.
from abc import ABC, abstractmethod


class CheckTheNumber(ABC):
    @abstractmethod   # код будет работать только если в дочерних классах прописан нижеуказанный метод
    def to_accept(self, ware, quant):
        pass


class Warehouse(CheckTheNumber):
    def __init__(self, name_warehouse):
        self.name_warehouse = name_warehouse
        self.structure = {}

    def __str__(self):
        return f'{self.structure}'

    def __iter__(self):  # магический метод для итерации (вывод словаря построчно)
        print('На складе хранится:')
        return (f'{key}: {val} шт.' for key, val in self.structure.items())

    def to_accept(self, ware, quant):  # принять товар на склад
        if isinstance(quant, int):  # проверка на принадлежность переменной к определенному типу
            if ware in self.structure:
                self.structure[ware] += quant
            else:
                self.structure[ware] = quant
            return f'Товар {ware} {quant} шт. принят на склад.'
        else:
            return f'Неверное значение "{quant}". Должно быть число!'

    def output(self, ware, quant):  # передача товара кому-либо (убираем со склада)
        if ware in self.structure:
            if self.structure[ware] < quant:
                return f'Товар {ware} в кол-ве {quant} шт. отсутствует на складе. В наличии {self.structure[ware]} шт.'
            else:
                self.structure[ware] -= quant
                if self.structure[ware] == 0:
                    self.structure.pop(ware)
                return f'Товар {ware} {quant} шт. убран со склада.'
        else:
            return f'Товар {ware} отсутствует на складе.'


class OfficeAppliances:
    def __init__(self, name_ware, model, connection, price):
        self.name_ware = name_ware
        self.model = model
        self.connection = connection
        self._price = price

    @property  # делает атрибут price только для чтения
    def price(self):  # геттер для чтения защищенной переменной
        return self._price

    @price.setter  # сеттер для замены значения защищенной переменной
    def price(self, value):
        if isinstance(value, int):
            print(f'Цена поменялась c {self._price} на {value}')
            self._price = value
        else:
            print('Цена не поменялась, так как введено не число!')


class Printer(OfficeAppliances):
    def __init__(self, name_ware, model, connection, _price, color, printing):
        super().__init__(name_ware, model, connection, _price)
        self.color = color
        self.printing = printing

    def __str__(self):
        return f'{self.__class__.__name__} {self.model} {self.connection} {self._price} {self.color} {self.printing}'


class Scanner(OfficeAppliances):
    def __init__(self, name_ware, model, connection, _price, types):
        super().__init__(name_ware, model, connection, _price)
        self.types = types

    def __str__(self):
        return f'{self.__class__.__name__} {self.model} {self.connection} {self._price} {self.types}'


class Xerox(OfficeAppliances):
    def __init__(self, name_ware, model, connection, _price, efficiency, color):
        super().__init__(name_ware, model, connection, _price)
        self.efficiency = efficiency
        self.color = color

    def __str__(self):
        return f'{self.__class__.__name__} {self.model} {self.connection} {self._price} {self.efficiency} {self.color}'


storage = Warehouse('Склад оргтехники')
print('Склад открыт.')
subject_1 = Printer('Принтер', 'HP', 'проводное/беспроводное подключение', '5300', 'цветной', 'лазерная печать')
print(vars(subject_1))  # вывод всех значений переменной
print(storage.to_accept(str(subject_1), 1))  # добавляем товар на склад (правильно)
print(storage.to_accept(str(subject_1), '2'))  # добавляем товар на склад (неправильно: т.к. введено не число)
print(storage.to_accept(str(subject_1), 4))  # добавляем такой же товар на склад (происходит суммирование кол-ва товара)
subject_2 = Scanner('Сканер', 'Canon', 'проводное подключение', '1200', 'ч/б')
subject_2.price = '1234'  # меняем значение защищенной переменной (исп. сеттер) (неправильно: должно быть число)
print(subject_2.price)  # вывод цены (цена не изменится) (исп. геттер)
subject_2.price = 4321  # меняем значение защищенной переменной (исп. сеттер) (правильно: введено число, а не строка)
print(subject_2.price)  # вывод цены (цена поменяется) (исп. геттер)
print(storage.to_accept(str(subject_2), 2))  # добавляем товар на склад
print(storage.output(str(subject_2), 4))  # убираем товар со склада (проверка на количество не пройдена)
print(storage.output(str(subject_2), 1))  # убираем товар со склада (проверка на количество пройдена)
subject_3 = Xerox('Ксерокс', 'ProfiLine', 'проводное подключение', '2850', '20 стр/мин', 'цветной')
storage.to_accept(str(subject_3), 2)  # товар добавится на склад, но в консоль не будет выведено сообщение об этом
print(subject_3.price)  # вывод защищенной переменной (с помощью геттера)
for item in storage:  # вывод состава склада
    print(item)
print('Склад закрыт.')
