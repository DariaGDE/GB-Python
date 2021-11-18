with open('data_from_user.txt', 'w') as f:
    while True:
        text = input("Введите информацию для записи в файл: ")
        if text:
            f.write(text + '\n')
        else:
            break
