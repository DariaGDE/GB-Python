list_of_lists_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_of_lists_2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

class Matrix:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        '\n'.join(map(str, self.list_of_lists))

    def __add__(self, other):
        result = []
        for stroka in range(len(self.list_of_lists)):
            result.append([])
            for element in range(len(self.list_of_lists[0])):
                result[stroka].append(self.list_of_lists[stroka][element] + other.list_of_lists[stroka][element])
        return '\n'.join(map(str, result))



matrix_1 = Matrix(list_of_lists_1)
matrix_2 = Matrix(list_of_lists_2)
print(matrix_2 + matrix_1)