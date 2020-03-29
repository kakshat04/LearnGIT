def Test1(a):
    # assert a<10 # if condition is true, return a, else return assertion4

    if 0 <= a <= 10:
        return "AAA"
    elif a > 10:
        return "BBB"
    else:
        # raise AssertionError("check number")
        assert False, "CCC"
    return a

z = Test1(10)
print(z)


names = ["A",
         "B",
         "C",]
print(names)


from Understanding_Underscores import *
# print(internal1)
z = A()
print(z._internal())


def int_to_Roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        # print(num, val[i])
        # print(num//val[i])
        for k in range(num // val[i]):
            print(i)
            print(val[i])
            roman_num = roman_num + syb[i]
            print(roman_num)
            num = num - val[i]
        i += 1
    return roman_num

int_to_Roman(1)


# Learning DICT
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict['model'])
print(thisdict.get('model'))
thisdict['model'] = 'Figo'
print(thisdict)

for x in thisdict:
    print(thisdict[x])

if "brand" in thisdict:
    print("Yes")

# print(len(thisdict))
# thisdict.pop("model")
# print(thisdict)


thisdict.popitem()
print(thisdict)
del thisdict['model']
print(thisdict)

# thisdict.clear()
# print(thisdict)

thisdict1 = thisdict.copy()
print(thisdict1)

z = dict(thisdict1)
print(z)


class A:
    def __init__(self, a):
        self.a = a

    # def __str__(self):
    #     return "Inside A"

    def method(self):
        return "Inside Instance method"

    @classmethod
    def cls_method(cls):
        return "Inside class Method"

    @staticmethod
    def static_method():
        return "Inside Static method"

obj1 = A(10)
print(A.cls_method())


def upper(func):
    def wrapper():
        return func().upper()
    return wrapper

@upper
def abc():
    return "a"

def def_():
    return "b"


print(abc())
print(def_())

# Generator function
l1 = [1,2,3,4]
# l2 = [1,4,9,16]
def abc(l1):
    l2 = list(map(lambda x: x**2, l1))
    for i in l2:
        yield i

obj = abc(l1)
for i in obj:
    print(i)
# print(next(obj))
# print(next(obj))
# print(next(obj))

x = (x**2 for x in l1)
print(next(x))
print(next(x))
print(next(x))

l3 = iter(l1)
print(next(l3))

class A:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num

p = A(3)
z = iter(p)

print(next(z))




