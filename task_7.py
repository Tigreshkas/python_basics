# Реализовать проект «Операции с комплексными числами».

class ComplexNum:
    def __init__(self, num_compl):
        for symbol in num_compl:
            if symbol == '+' or symbol == '-':
                ind = num_compl.index(symbol)
                a = int(num_compl[0:ind])
                b = int(num_compl[ind:-1])
                self.num_compl = [a, b]

    def __str__(self):
        return f'{self.num_compl[0]}{self.num_compl[1]:+}i'

    def __add__(self, other):  # перегрузка метода сложения
        res = list(map(lambda x, y: x + y, self.num_compl, other.num_compl))
        return f'{res[0]}{res[1]:+}i'

    def __mul__(self, other):  # перегрузка метода умножения
        a = self.num_compl[0]
        b = self.num_compl[1]
        c = other.num_compl[0]
        d = other.num_compl[1]
        return f'{a * c - b * d}{a * d + b * c:+}i'


num_1 = ComplexNum('2+5i')
num_2 = ComplexNum('3-4i')
print(f'{num_1} - комплексное число N1')
print(f'{num_2} - комплексное число N2')
print(f'{num_1 + num_2} - сумма комплексных чисел')
print(f'{num_1 * num_2} - произведение комплексных чисел')
