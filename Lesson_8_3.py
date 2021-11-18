class IsListOfNumbers(Exception):

    def __init__(self, txt_of_error):
        self.txt_of_error = txt_of_error

new_list = []
while True:
    users_input = input("Введите число -  ")
    if users_input != 'stop':
        try:
            if not users_input.isdigit():
                raise IsListOfNumbers('Не число')
            else:
                new_list.append(int(users_input))
        except IsListOfNumbers as e:
            print(e)
    else:
        break
print(new_list)
