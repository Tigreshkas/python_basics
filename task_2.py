# Реализовать класс Road (дорога).

class Road:
    def __init__(self, length, width, weight=25, thickness=0.005):
        self._length = length
        self._width = width
        self._weight = weight
        self._thickness = thickness

    def calculation(self):
        result = self._length * self._width * self._weight * self._thickness
        print(f'Для покрытия участка дороги длиной {self._length}м и шириной {self._width}м '
              f'потребуется {int(result)}кг асфальта.')


part_road = Road(5000, 20)
part_road.calculation()
