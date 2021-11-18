# with open('hw_5_2.txt', 'w+') as f:
#     f.write("Yesterday\nAll my troubles seemed so far away\nNow it looks as though they\'re here to stay\nOh, I believe in yesterday")
with open('hw_5_2.txt', 'r') as f:
    i = 0
    for line in f:
        print(line.split())
        print(f'Количество слов в строке - {len(line.split())}')
        i += 1
    print(f'Общее количество строк - {i}')
