def func_divide():
    try:
        a = int(input("Введите число(делимое) - "))
        b = int(input('Введите число(делитель) - '))
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("На ноль делить нельзя")

    except:
        print("Нужно ввести числа")


print(func_divide())
