# #################  What do you know about palindromes? Can you implement one in Python? #########################
def palindrome(inp):
    rev = ""
    for i in range(len(str(inp))-1, -1, -1):
        rev += str(inp)[i]
    if rev == str(inp):
        return "Palindrome"
    else:
        return "Not Palindrome"


def palindrome_generator(inp):
    # rev = ""
    dict1 = {}
    for k in inp:
        # print(k)
        rev = ""
        for i in range(len(str(k))-1, -1, -1):
            rev += str(k)[i]
        # print(rev)
        if rev == str(k):
            dict1[(k, rev)] = "Palindrome"
            # yield "Palindrome"
            yield dict1
        else:
            dict1[(k, rev)] = "Not Palindrome"
            # yield "Not Palindrome"
            yield dict1


check_palindrome = palindrome("CCCC")
print(check_palindrome)

input_list = [1421, "hannah", 123, "Akshat", 141, 1551, 123341]
check_palindrome_gen = palindrome_generator(input_list)
for i in range(len(input_list)):
    print(next(check_palindrome_gen))


# ##################### What do you mean by *args and **kwargs? ########################################
"""
New learning - If we pass same alphabet required parameter and  for **kwargs' key, it will give error
def test(a, *args, **kwargs):
    print(a, args, kwargs)


test(10, 20, 30, 40, a=100, a=200)

"""
class Test1:
    def __init__(self, a, b=0, *args, **kwargs):
        self.a = a
        self.b = b
        self.aaa = args
        self.bbb = kwargs

    def check_args(self, *args):
        print(self.a)
        print(self.b)
        print(self.aaa)
        print(self.bbb)
        print(args)


def test(a, *args, **kwargs):
    print(a, args, kwargs)


obj1 = Test1(10, 20, 30, 40, 2.0, 3.0, 4.0, k1=100, k2=200)
obj1.check_args(111, 222)
test(10, 20, 30, 40, k1=100, k2=200)


# ############################ What is a closure in Python? #########################################
# Let's learn more about inner functions
def outer(num1):
    if not isinstance(num1, int):
        return "number is not integer"

    def inner(num11):
        return num11 + 1
    return inner(num1)


print(outer(10))
# print(inner(20))


def factorial(number):
    if not isinstance(number, int):
        return "Input is not a number"
    elif number <= 0:
        return "Number should be greater than 0"
    elif number == 1:
        return 1

    def inner_fact(num):
        fact = 1
        for i in range(1, num+1):
            fact = fact*i
        return fact
    return inner_fact(number)


print(factorial(5))

# Let's see closure


def aa(n1):
    def bb():
        return n1+2

    def cc(n3):
        return n1 + n3
    return cc


print(aa(10)(2))
print()


def func1(name):
    def func2(name1):
        return "Hello " + name1
    return func2(name)


z = func1("Kumar")
print(z)

# ########################### Are these statements optimal? If not, optimize them. ############################

word = 'word'
print(word.__len__())
# print(help(word.__len__()))  # if we check this, __len__() will call len(), using len(word) is optimised
print(len(word))

# ######################## What is the iterator protocol? ######################################
# Lets use both iterator and Generator
# Generator are of 2 types, i- Generator Method ii- Generator Expression
# i- Generator Method:


def test_generator_method(num):
    for i in range(num):
        yield i


z = test_generator_method(3)
print(next(z))
print(next(z))
print(next(z))
# print(next(z))  # as max input is 3, 4th next will give stop iteration error

# ii- Generator syntax
z = (x**2 for x in range(4))
z1 = iter([x**2 for x in range(4)])
print("Iterator syntax")
print(next(z1))
print(next(z1))
print(next(z1))
print(next(z1))

print("Gererator syntax")
print(next(z))
print(next(z))
print(next(z))
print(next(z))

# ################### What is tuple unpacking? ##################
tup = (1, 2, 3)
a, b, c = tup  # This is called Tuple Packing
print(a)
print(b)
print(c)


# #################### What will the following code output? ################################
a = 1
a, b = a + 1, a + 1
print(a, b)  # 2,2

a1 = 1
a1 = a1 + 1
b1 = a1 + 1
print(a1, b1)  # 2,3


# ######################## What is a frozen set in Python? ############################
set1 = set([1, 2, 3, 4, 4])
set1.remove(4)
print(set1)

f_set = frozenset([1, 2, 3, 4])
print(f_set.union(set1))

l1 = [1,2,3,4,5,6,23,324,23,53,242,35324]
l2 = [1,2,4,14,124,123,14,124,1221,242,412]

z = list(set(l1).intersection(set(l2)))
print(z)


# ################### How will you use Python to read a random line from a file? #################
with open("file1.txt", 'a+') as wf:
    for i in range(10):
        wf.write("sjhdjkashd " + str(i) + "\n")

import random
with open('file1.txt', 'r+') as rf:
    print(random.choice(rf.readlines()))


# ######################## What is JSON? Describe in brief how you’d convert JSON data into Python data? ##########
import json
d1 = {'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}
d2 = {'name': 'Larry', 'website': 'google.com', 'from': 'Michigan'}
d3 = {'name': 'Tim', 'website': 'apple.com', 'from': 'Alabama'}
data = {}
data['people'] = []
data['people'].append(d1)
data['people'].append(d2)
data['people'].append(d3)
print(data)

with open("json_file.txt", 'w') as wf:
    json.dump(data, wf)

with open("json_file.txt", 'r') as rf:
    data = json.load(rf)
    print(data)
    for k in data['people']:
        print(k)
        print(k['name'])
        print(k['website'])
        print(k['from'])
