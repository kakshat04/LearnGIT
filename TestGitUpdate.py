def capital(text):
    return text.upper()


def make_changes(func, text1):
    """
    Passing function as parameter
    :param func:
    :param text1:
    :return:
    """
    if text1.isupper():
        return text1
    else:
        return func(text1)


print(capital("abc"))

print(make_changes(capital, "Bxx"))

print(make_changes(capital, "Bxx"))


"""
Function can be nested
"""


def test_nested(text):
    def nested(t):
        return t.upper()
    return nested(text)


def test_nested_number(inp):
    if inp is "Mod":
        def find_mod(num):
            if num < 2:
                return "Invalid Number, number should be greater than 2"
            return num % 2
        return find_mod
    elif inp is "Div":
        def find_div(num):
            if num < 2:
                return "Invalid Number, number should be greater than 2"
            return num / 2
        return find_div
    else:
        return "Input should be 'Mod' or 'Div'"


print(test_nested("kumar akshat"))
z = test_nested_number("Div")
print(z(5))


"""
Lambda
"""


def add(a, b):
    return a + b


z = (lambda x, y: x + y)(10,20)
print(z)
# print(add1(10, 20))

<<<<<<< HEAD
=======

"In Python 2, map, reduce and filter returned List itself, whereas in Python 3, it returns an object."
import functools
test_list = [10, 50, 51, 0, 51, 210, 4, 21, 54, 50]
add = functools.reduce(lambda x, y: x + y, test_list)
print(add)
mod = list(filter(lambda x: x % 2 == 0, test_list))
print(mod)
mul = tuple(map(lambda x: x**2, test_list))
print(mul)

>>>>>>> LearnGit
