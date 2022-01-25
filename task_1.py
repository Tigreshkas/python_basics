# Создать класс TrafficLight (светофор).
import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color  # приватный атрибут

    def running(self):
        minings = vars(self)  # объекту присваиваем введенный информацию
        if minings['_TrafficLight__color'] == 'Red':  # проверяем какое значение у ключа с цветом и выводим результат
            print(f'Красный сигнал светофора!')
            time.sleep(7)  # время ожидания до следующей команды
            print(f'Желтый сигнал светофора!')
            time.sleep(2)
            print(f'Зеленый сигнал светофора!')
            time.sleep(3)
        elif minings['_TrafficLight__color'] == 'Yellow':
            print(f'Желтый сигнал светофора!')
            time.sleep(2)
            print(f'Зеленый сигнал светофора!')
            time.sleep(3)
            print(f'Красный сигнал светофора!')
            time.sleep(7)
        else:
            print(f'Зеленый сигнал светофора!')
            time.sleep(3)
            print(f'Красный сигнал светофора!')
            time.sleep(7)
            print(f'Желтый сигнал светофора!')
            time.sleep(2)


light_green = TrafficLight('Green')  # создаем несколько объектов с одним атрибутом
light_yellow = TrafficLight('Yellow')
light_red = TrafficLight('Red')
light_red.running()  # вызываем метод running (в зависимости от первого цвета)
# light_yellow.running()
# light_green.running()
