velocity = int(input('Введите скорость в автомобиля в км/ч - '))
time = int(input('Введите время в пути в минутах - '))

distance = round(((velocity * 1000 /(60 ** 2)) * (time * 60)) / 1000, 2)
print('Вы проехали {} км.'.format(distance))
