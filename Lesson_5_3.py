with open('wage.txt', 'r') as f:
    dict_of_employees = {line.split()[0]: int(line.split()[1]) for line in f}
    print(f'Средняя зарплата - {round(sum(dict_of_employees.values())/len(dict_of_employees), 2)}')
    print(f'Список сотрудников с зарплатой меньше 20 000 - '
          f'{[el[0] for el in dict_of_employees.items() if el[1] <= 20000 ]}')

print(dict_of_employees)
