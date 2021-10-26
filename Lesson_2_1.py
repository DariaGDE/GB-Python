new_list = ['text', 12345, 77.8, ('a','b'), [34, 33, 36], complex(2,1), {'key_1':'value_1', 'key_2':'value_2'}]
for i in range(len(new_list)):
    print(f'Тип данных элемента списка с номером {i} - {type(new_list[i])}')
for el in new_list:
    print(f'Тип данных элемента {el} - {type(el)}')
    