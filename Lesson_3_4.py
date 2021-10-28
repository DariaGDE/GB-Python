def power(x,y):
    return x**(y)

print(power(2,-1))

def power_2(x,y):
    if y < 0:
        print("Отрицательная степень")
        i = 1
        result = 1
        while i <= abs(y):
            result /=  x
            i += 1
        return result
    else:
        print("Положительная степень")
        i = 1
        result = 1
        while i <= y:
            result *= x
            i += 1
        return result

print(power_2(4,-1))
print(power_2(3,4))
print(power_2(-1,-1))
