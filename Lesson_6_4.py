class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Автомобиль {self.name} начал движение.')
    def stop(self):
        print(f'Автомобиль {self.name} остановился.')
    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}.')
    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60}')
        else:
            print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч.')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40} км/ч')
        else:
            print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)
        print(f'Автомобиль {self.name} - машина полиции')

class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def fast(self, competitor):
        print(f'Автомобиль {self.name} обгоняет {competitor.name} на {self.speed - competitor.speed} км/ч.')


nissan = PoliceCar(70, 'white', 'Nissan X-Trail')
print(nissan.is_police)
nissan.go()
nissan.stop()
nissan.turn('направо')
nissan.show_speed()

porshe = SportCar(180, 'red', 'Porshe 718 Boxter S')
porshe.fast(nissan)