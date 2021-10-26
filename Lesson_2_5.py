# Рейтинг
my_list = [7, 5, 3, 3, 2]
new_number =int(input("Введите число "))
new_pos = 0
for i, el in enumerate(my_list):
    if el >= new_number:
        new_pos = i + 1
my_list.insert(new_pos, new_number)
# print(new_pos)
print(my_list)

