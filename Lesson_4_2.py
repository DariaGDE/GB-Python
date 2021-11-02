list_of_numbers = [0,7,12,88,3,6,2,1,90,8]
new_list = [list_of_numbers[i] for i in range(1,len(list_of_numbers)) if list_of_numbers[i] > list_of_numbers[i-1]]
print(new_list)
