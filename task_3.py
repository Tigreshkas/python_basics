# Осуществить программу работы с органическими клетками, состоящими из ячеек.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity >= other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            raise ValueError('Разность клеток отрицательная.')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity / other.quantity)

    def make_order(self, row):
        result = ['*' * row] * (self.quantity // row)
        if self.quantity % row:
            result.append('*' * (self.quantity % row))
        return '\n'.join(result)


cell_1 = Cell(10)
cell_2 = Cell(2)
print(cell_1.quantity + cell_2.quantity)
print(cell_1.quantity - cell_2.quantity)
print(cell_1.quantity * cell_2.quantity)
print(cell_1.quantity / cell_2.quantity)
print(cell_1.make_order(5))
