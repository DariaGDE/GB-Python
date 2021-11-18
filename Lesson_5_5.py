with open('new_file_2.txt', 'w') as f:
    f.write('1 2 3 4 5 6 7 8 9 10')
with open('new_file_2.txt', 'r') as f:
    new_list = [int(el) for el in f.readline().split()]
    print(sum(new_list))
