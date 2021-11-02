list_of_random_nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in list_of_random_nums if list_of_random_nums.count(el) == 1]
print(new_list)
