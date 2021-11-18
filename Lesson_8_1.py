class Date:

    def __init__(self, day=14, month = 1, year = 1988):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def iterpreter(cls, users_string):
        day, month, year = map(int, users_string.split('-'))
        new_date = cls(day, month, year)
        return new_date

    @staticmethod
    def is_date_valid(date_string_for_check):
        day, month, year = map(int, date_string_for_check.split('-'))
        if day <= 31 and month <= 12 and year <= 10000:
            print(f'Проверка даты пройдена успешно: день - {day}, месяц - {month}, год -{year}')


birthday = Date.iterpreter('27-07-1988')
print(birthday.year)
print(birthday.month)
print(birthday.day)
Date.is_date_valid('12-8-2050')
