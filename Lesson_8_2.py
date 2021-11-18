class DivisionZero(Exception):

    def __init__(self, text_of_error):
        self.text_of_error = text_of_error


users_input_1 = int(input("Введите первое число(делимое) - "))
users_input_2 = int(input("Введите первое число(делимое) - "))

try:
    if users_input_2 == 0:
        raise DivisionZero('Деление на ноль')
    else:
        result = users_input_1 / users_input_2
        print(result)
except ValueError:
    print('Введите число')
except DivisionZero as e:
    print(e.text_of_error)
