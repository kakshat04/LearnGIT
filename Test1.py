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