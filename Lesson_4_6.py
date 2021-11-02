from itertools import count, cycle
from random import shuffle

new_list = []
for el in count(int(input("Введите число - "))):
    if el <=10:
        new_list.append(el)
    else:
        break
print(new_list)

list_of_symbols = ['a', 'B', 'c', 'D', 'e', 'F', 'g']
c = 0
# shuffle(list_of_symbols)
for el in cycle(list_of_symbols):
    if c > 9:
        break
    print(el)
    c += 1



