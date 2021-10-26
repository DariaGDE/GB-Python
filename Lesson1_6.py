dist_at_first = int(input('Введите дистанцию в первый день '))
dist_desirable = int(input('Введите дистанцию, которую нужно достичь '))
number_of_days = 1
dist_final = dist_at_first
while dist_final < dist_desirable:
    dist_final += dist_final * 0.1
    number_of_days += 1
    print(dist_final)
print("Количество дней - ", number_of_days)
