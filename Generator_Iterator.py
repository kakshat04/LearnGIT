# Generator Function
def fibonacci(value):
    a, b = 0, 1
    count = 0
    while count < value:
        yield a
        c = a + b
        a = b
        b = c
        count += 1


fib = fibonacci(3)
print(next(fib))
print(next(fib))
print(next(fib))


def sort(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(0, len(list_to_sort) - 1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
        yield list_to_sort


z = sort([123,23,51,451,415,1234,15124,1])
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))


# Generator Expression
list1 = [4, 16, 64, 256]
list_comp = [a ** (1/2) for a in list1]
print(list_comp)


gen_exp = (a ** (1/2) for a in list1)
print(gen_exp)
print(next(gen_exp))
print(next(gen_exp))
