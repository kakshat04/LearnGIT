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