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
