class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
       return f'{self.name} {self.surname}'
    def total_income(self):
        return sum(self._income.values())
new_employee = Position('Tom', 'Harrington', 'accountant', 4000, 500)
print(new_employee.get_full_name())
print(new_employee.total_income())

