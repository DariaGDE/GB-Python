class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def mass_of_asphalt(self, number_of_layers):
        return f'Масса асфальта новой дороги шириной {self._length} м длиной {self._width} м и ' \
               f'с количеством слоев {number_of_layers} ' \
               f'- {(self._length * self._width * 25 * number_of_layers)/1000} т.'

new_road = Road(5000, 20)
print(new_road._length, new_road._width)
print(new_road.mass_of_asphalt(5))
