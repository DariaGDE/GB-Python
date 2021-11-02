from functools import reduce
list_of_num = [el for el in range(100,1001,2)]
print(list_of_num)
def func_1(prev_el, el):
    return prev_el * el
print(reduce(func_1, list_of_num))

# result = 1
# for el in list_of_num:
#     result *= el
    # print(result)
