# Реализовать класс Stationery (канцелярская принадлежность).

class Stationery:  # родительский класс
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):  # дочерний класс
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Пишем текст')


class Pencil(Stationery):  # дочерний класс
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем график')


class Handle(Stationery):  # дочерний класс
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Выделяем нужную информацию')


draw_chalk = Stationery('Chalk')
print(draw_chalk.title)
draw_chalk.draw()

draw_pen = Pen('Pen')
print(draw_pen.title)
draw_pen.draw()

draw_pencil = Pencil('Pencil')
print(draw_pencil.title)
draw_pencil.draw()

draw_handle = Handle('Handle')
print(draw_handle.title)
draw_handle.draw()
