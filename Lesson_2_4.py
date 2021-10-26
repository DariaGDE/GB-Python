user_inp = input("Введите слова через пробел: ").split()

for i, el in enumerate(user_inp):
    print(i, el[:10])