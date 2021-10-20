time_in_sec = int(input('Введите время в секундах - '))
hours = time_in_sec // (60 ** 2)
minutes = (time_in_sec % (60 ** 2)) // 60
seconds = (time_in_sec % (60 ** 2)) % 60
print('Время {} часов {} минут {} секунд.'.format(hours,minutes,seconds))
