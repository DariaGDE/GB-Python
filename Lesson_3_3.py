def sum_of_max(num1, num2, num3):
    list_new = [num1, num2, num3]
    return sorted(list_new, reverse=True)[0] + sorted(list_new, reverse=True)[1]
print(sum_of_max(1,2,3))
print(sum_of_max(7,0,3))

