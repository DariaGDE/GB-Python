new_list = {}
with open('new_file_3.txt', 'r') as f:
    for line in f:
        subject, schedule = line.split(":")
        hours = [i for i in schedule if i == " " or (i >='0' and i <='9')]
        # print(hours)
        subject_sum = sum(map(int, ''.join(hours).split()))
        # print(subject_sum)
        new_list[subject] = subject_sum
print(new_list)
