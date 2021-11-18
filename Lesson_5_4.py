translation = ['Один', 'Два', 'Три', 'Четыре']
counters = []
with open('new_file.txt', 'r') as f:
    for line in f:
        print(line, end='')
        counters.append(line.split()[-1])
with open('new_file_1.txt', 'w') as f:
    for i in range(len(translation)):
        f.write(f'{translation[i]} - {counters[i]} \n')
