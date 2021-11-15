from abc import ABC, abstractclassmethod

class Clothers:
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    @abstractclassmethod
    def amount_of_material(self):
        pass

    def __add__(self, other):
        return self.amount_of_material + other.amount_of_material


class Costume(Clothers):
    @property
    def amount_of_material(self):
        return round((self.parameter * 2 + 0.3)/100, 2)
class Coat(Clothers):
    @property
    def amount_of_material(self):
        return round((0.5 + self.parameter/6.5),2)

new_costume = Costume(156)
new_coat = Coat(7)
print(new_costume.amount_of_material)
print(new_coat.amount_of_material)
print(new_coat + new_costume)