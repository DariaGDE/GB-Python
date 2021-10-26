user_number = input('Введите любое положительное число  ')
max_number = 0
for i in range(len(user_number)):
    if int(user_number[(i-1)]) > max_number:
        max_number = int(user_number[(i-1)])
print('Самая большая цифра в вашем числе {}.'.format(max_number))
