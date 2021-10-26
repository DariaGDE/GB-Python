# через словарь
seasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5],
           'Осень': [9, 10, 11], 'Лето': [6, 7, 8]}
month = int(input("Введите порядковый номер месяца для проверки времени года - "))
for k,v in seasons.items():
    if month in v:
        print(k)


# через списки
seasons_list = [['Зима', 1, 2, 12], ['Весна', 3, 4, 5],
                ['Осень',9, 10, 11], ['Лето', 6, 7, 8]]
month_new = int(input("Введите месяц еще раз - "))
for i in range(len(seasons_list)):
    if month_new in seasons_list[i]:
        print(seasons_list[i][0])


