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


"In Python 2, map, reduce and filter returned List itself, whereas in Python 3, it returns an object."
import functools
test_list = [10, 50, 51, 0, 51, 210, 4, 21, 54, 50]
add = functools.reduce(lambda x, y: x + y, test_list)
print(add)
mod = list(filter(lambda x: x % 2 == 0, test_list))
print(mod)
mul = tuple(map(lambda x: x**2, test_list))
print(mul)


"Difference between == and is"
a = [1, 2, 3]
b = a

print(a)
print(b)
print(b == a)  # This checks for equality
print(b is a)  # This checks for identity ==> Object pointer
# Both will return True as both content of list and object pointer is same.

c = list(a)
print(c)
print(a == c)  # This will return True, as it checks for equality
print(b == c)  # This will return True, as it also checks for equality
print(b is c)  # This will return False, as c will point to different object.
print(a is c)  # This will return False, as c will point to different object.


# Keyword arguments
def test_arguments(aa, dd=0, *bb, **cc):
    print(aa, dd, bb, cc)


test_arguments(10, 20, 30, a=1, b=2)


# Decorators
def base_function(func):
    def wrapper():
        return "ABC" + func() + "ABC"
    return wrapper


def sec_base_func(func):
    def wrap():
        return "abc" + func() + "abc"
    return wrap


@sec_base_func
@base_function
def test():
    return "Hello World"


def dec_call_test(func):
    def wrap(text):
        return func(text).upper()
    return wrap

@dec_call_test
def test1(text):
    return text


@dec_call_test
def test2(text1):
    return text1


# @dec_call_test
def test3(text2):
    return text2


def call_test():
    print(test1("akshat").upper())
    print(test2("paru").upper())
    print(test3("moti").upper())


call_test()
print(test1("akshat"))
print(test2("paru"))
print(test3("chotu"))
