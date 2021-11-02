from functools import reduce
def fact(n):
    lst = [el for el in range(1,n+1)]
    def func_1(prev_el, el):
        return prev_el * el
    return reduce(func_1, lst)
print(fact(4))

def gener(n):
    for el in range(1,n+1):
        yield fact(el)
        print("Done")
example = gener(4)
print(next(example))
print(next(example))
print(next(example))
print(next(example))

