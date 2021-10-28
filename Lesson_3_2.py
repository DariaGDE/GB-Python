
def personality(name=' ', last_name=' ', year_of_birth = None, city=' ', email=' ', phone_number= None):
   print(name, last_name, year_of_birth, city, email, phone_number)

personality(name = 'Nick', last_name='Cruse', year_of_birth=1988, city='Moscow', email='n_cruse@gmail.com',
            phone_number=99902976528)


def personality_2(**kwargs):
    for k, v in kwargs.items():
        print(f'{k.title()} - {v}', end=' ')

personality_2(name='Tom', last_name='Stone', phone_number=99980000889)



