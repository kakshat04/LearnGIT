"""
Functions are first class in python
i.e It can be stored in a variable
    It can be stored in Data Structure
    It can be passed as function parameter
    It can be returned as values from another function
"""


def yell(text):
    return text.upper()


print(yell("hello"))

"""
Since everything in Python is an object, so is function yell, hence it can be assigned to another variable
"""

bark = yell

print(bark("woof"))


del yell
"""
even if we delete yell, bark can still be used to as an object
"""
# print(yell("test"))
print(bark("test1"))

funcs = [bark, str.lower, str.capitalize]
print(funcs)

for f in funcs:
    print(f, f("yess"))
print(funcs[0]("heyy"))


# Functions can be used as parameters
def greet(func):
    return func("testing function inside function")


print(greet(bark))


def sum(a, b):
    return a + b

def test(function, a,b):
    mul = a*b
    sum = function(a,b)
    return mul, sum


print(test(sum, 10, 20))



