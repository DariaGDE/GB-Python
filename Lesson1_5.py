revenue = int(input('Введите выручку в рублях - '))
spends = int(input('Введите траты в рублях - '))
fin_result = revenue - spends
print('Ваш финансовый результат состаавил ', fin_result)
if fin_result > 0:
    profit = fin_result / revenue
    print("Рентабельность составила ", profit)
number_of_employees = int(input("Введите количество сотрудников  "))
print('Выручка на человека составила {}'.format(fin_result/number_of_employees))
