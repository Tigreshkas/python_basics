# Реализуйте базовый класс Car.

class Car:  # родительский класс
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):  # функции родительского класса
        print('Go-go')

    def stop(self):
        print('Stop car')

    def turn(self):
        print('Car turn')

    def show_speed(self):
        print(f'Current vehicle speed is {self.speed}')


class TownCar(Car):  # дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):  # функция выводит скорость. Если скорость превышена, то выводит сообщение о превышении.
        if self.speed >= 60:
            print('Speed limit!')
        else:
            print(f'Current vehicle speed is {self.speed}')


class SportCar(Car):  # дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):  # дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):  # функция выводит скорость. Если скорость превышена, то выводит сообщение о превышении.
        if self.speed >= 40:
            print('Speed limit!')
        else:
            print(f'Current vehicle speed is {self.speed}')


class PoliceCar(Car):  # дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


auto_1 = TownCar(50, 'black', 'Tesla', 'False')  # создаем объект с несколькими атрибутами
print(vars(auto_1))  # выводим результат (все атрибуты)
print(auto_1.name)  # выводим определенный атрибут
auto_1.go()  # вызываем метод
print(auto_1.speed)
auto_1.show_speed()
auto_1.stop()

auto_2 = SportCar(100, 'red', 'Audi R8', 'False')
print(vars(auto_2))
print(auto_2.name)
print(auto_2.color)

auto_3 = WorkCar(50, 'grey', 'Lada Largus', 'False')
print(vars(auto_3))
print(auto_3.name)
auto_3.go()
auto_3.turn()
print(auto_3.speed)
auto_3.show_speed()
auto_3.stop()

auto_4 = PoliceCar(70, 'white', 'Ford Focus', 'True')
print(vars(auto_4))
print(auto_4.name)
print(auto_4.is_police)
auto_4.go()
auto_4.turn()
auto_4.stop()
