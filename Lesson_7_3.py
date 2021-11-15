class Cell:
    def __init__(self, capacity):
        self.capacity = int(capacity)

    def __add__(self, other):
        return self.capacity + other.capacity

    def __sub__(self, other):
        if self.capacity < other.capacity:
            return 'Разность ячеек меньше 0'
        else:
            return self.capacity - other.capacity

    def __mul__(self, other):
        result = self.capacity * other.capacity
        return Cell(result).capacity

    def __truediv__(self, other):
        result = self.capacity // other.capacity
        return Cell(result).capacity

    def make_order(self, spots_in_row):
        result = self.capacity // spots_in_row
        result_2 = self.capacity % spots_in_row
        return '\n'.join(['*' * result for _ in range(result)]) + '\n' + '*' * result_2


alpha_1 = Cell(13)
alpha_2 = Cell(8)
print(alpha_1 + alpha_2)
print(alpha_1 - alpha_2)
print(alpha_1 * alpha_2)
print(alpha_1/alpha_2)
print(alpha_1.make_order(4))