new_string = input("Введите любые данные через пробел ")
input_list = new_string.split()
print(input_list)
for i in range(len(input_list)):
    if i % 2 !=0:
        input_list[i], input_list[i-1] = input_list[i-1], input_list[i]
print(input_list)
