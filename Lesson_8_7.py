class Complex:

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return f'{self.real_part + other.real_part} + {self.imaginary_part + other.imaginary_part}i'

    def __mul__(self, other):
        return f'{self.real_part * other.real_part - self.imaginary_part * other.imaginary_part} + ' \
               f'{self.real_part * other.imaginary_part + other.real_part * self.imaginary_part}i'


first_num = Complex(1, 2)
sec_num = Complex(2, 3)
print(first_num+sec_num)
print(first_num * sec_num)
