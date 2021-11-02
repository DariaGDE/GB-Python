from sys import argv
script_name, time_of_work, wage_per_hour, benefit = argv

salary = (int(time_of_work) * int(wage_per_hour)) + int(benefit)
print(f'Зарплата за {time_of_work} часов со ставкой {wage_per_hour} рублей за час и премией {benefit} рублей '
      f'составила {salary} рублей.')