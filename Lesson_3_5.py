result = 0
while True:
    new_list = input("Введите числа через пробел и нажмите Enter, для выхода нажмите Q - ").upper().split()
    if 'Q' not in new_list:
        new_list_1 = list(map(lambda x: int(x), new_list))
        result += sum(new_list_1)
    else:
        new_list = new_list[:new_list.index('Q')]
        new_list_1 = list(map(lambda x: int(x), new_list))
        result += sum(new_list_1)
        break
print(result)




