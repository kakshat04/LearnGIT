# # #################  What do you know about palindromes? Can you implement one in Python? #########################
# def palindrome(inp):
#     rev = ""
#     for i in range(len(str(inp))-1, -1, -1):
#         rev += str(inp)[i]
#     if rev == str(inp):
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
#
#
# def palindrome_generator(inp):
#     # rev = ""
#     dict1 = {}
#     for k in inp:
#         # print(k)
#         rev = ""
#         for i in range(len(str(k))-1, -1, -1):
#             rev += str(k)[i]
#         # print(rev)
#         if rev == str(k):
#             dict1[(k, rev)] = "Palindrome"
#             # yield "Palindrome"
#             yield dict1
#         else:
#             dict1[(k, rev)] = "Not Palindrome"
#             # yield "Not Palindrome"
#             yield dict1
#
#
# check_palindrome = palindrome("CCCC")
# print(check_palindrome)
#
# input_list = [1421, "hannah", 123, "Akshat", 141, 1551, 123341]
# check_palindrome_gen = palindrome_generator(input_list)
# for i in range(len(input_list)):
#     print(next(check_palindrome_gen))
#
#
# # ##################### What do you mean by *args and **kwargs? ########################################
# """
# New learning - If we pass same alphabet required parameter and  for **kwargs' key, it will give error
# def test(a, *args, **kwargs):
#     print(a, args, kwargs)
#
#
# test(10, 20, 30, 40, a=100, a=200)
#
# """
# class Test1:
#     def __init__(self, a, b=0, *args, **kwargs):
#         self.a = a
#         self.b = b
#         self.aaa = args
#         self.bbb = kwargs
#
#     def check_args(self, *args):
#         print(self.a)
#         print(self.b)
#         print(self.aaa)
#         print(self.bbb)
#         print(args)
#
#
# def test(a, *args, **kwargs):
#     print(a, args, kwargs)
#
#
# obj1 = Test1(10, 20, 30, 40, 2.0, 3.0, 4.0, k1=100, k2=200)
# obj1.check_args(111, 222)
# test(10, 20, 30, 40, k1=100, k2=200)
#
#
# # ############################ What is a closure in Python? #########################################
# # Let's learn more about inner functions
# def outer(num1):
#     if not isinstance(num1, int):
#         return "number is not integer"
#
#     def inner(num11):
#         return num11 + 1
#     return inner(num1)
#
#
# print(outer(10))
# # print(inner(20))
#
#
# def factorial(number):
#     if not isinstance(number, int):
#         return "Input is not a number"
#     elif number <= 0:
#         return "Number should be greater than 0"
#     elif number == 1:
#         return 1
#
#     def inner_fact(num):
#         fact = 1
#         for i in range(1, num+1):
#             fact = fact*i
#         return fact
#     return inner_fact(number)
#
#
# print(factorial(5))
#
# # Let's see closure
#
#
# def aa(n1):
#     def bb():
#         return n1+2
#
#     def cc(n3):
#         return n1 + n3
#     return cc
#
#
# print(aa(10)(2))
# print()
#
#
# def func1(name):
#     def func2(name1):
#         return "Hello " + name1
#     return func2(name)
#
#
# z = func1("Kumar")
# print(z)
#
# # ########################### Are these statements optimal? If not, optimize them. ############################
#
# word = 'word'
# print(word.__len__())
# # print(help(word.__len__()))  # if we check this, __len__() will call len(), using len(word) is optimised
# print(len(word))
#
# # ######################## What is the iterator protocol? ######################################
# # Lets use both iterator and Generator
# # Generator are of 2 types, i- Generator Method ii- Generator Expression
# # i- Generator Method:
#
#
# def test_generator_method(num):
#     for i in range(num):
#         yield i
#
#
# z = test_generator_method(3)
# print(next(z))
# print(next(z))
# print(next(z))
# # print(next(z))  # as max input is 3, 4th next will give stop iteration error
#
# # ii- Generator syntax
# z = (x**2 for x in range(4))
# z1 = iter([x**2 for x in range(4)])
# print("Iterator syntax")
# print(next(z1))
# print(next(z1))
# print(next(z1))
# print(next(z1))
#
# print("Gererator syntax")
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
#
# # ################### What is tuple unpacking? ##################
# tup = (1, 2, 3)
# a, b, c = tup  # This is called Tuple Packing
# print(a)
# print(b)
# print(c)
#
#
# # #################### What will the following code output? ################################
# a = 1
# a, b = a + 1, a + 1
# print(a, b)  # 2,2
#
# a1 = 1
# a1 = a1 + 1
# b1 = a1 + 1
# print(a1, b1)  # 2,3
#
#
# # ######################## What is a frozen set in Python? ############################
# set1 = set([1, 2, 3, 4, 4])
# set1.remove(4)
# print(set1)
#
# f_set = frozenset([1, 2, 3, 4])
# print(f_set.union(set1))
#
# l1 = [1,2,3,4,5,6,23,324,23,53,242,35324]
# l2 = [1,2,4,14,124,123,14,124,1221,242,412]
#
# z = list(set(l1).intersection(set(l2)))
# print(z)
#
#
# # ################### How will you use Python to read a random line from a file? #################
# with open("file1.txt", 'a+') as wf:
#     for i in range(10):
#         wf.write("sjhdjkashd " + str(i) + "\n")
#
# import random
# with open('file1.txt', 'r+') as rf:
#     print(random.choice(rf.readlines()))
#
#
# # ######################## What is JSON? Describe in brief how you’d convert JSON data into Python data? ##########
# import json
# d1 = {'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}
# d2 = {'name': 'Larry', 'website': 'google.com', 'from': 'Michigan'}
# d3 = {'name': 'Tim', 'website': 'apple.com', 'from': 'Alabama'}
# data = {}
# data['people'] = []
# data['people'].append(d1)
# data['people'].append(d2)
# data['people'].append(d3)
# print(data)
#
# with open("json_file.txt", 'w') as wf:
#     json.dump(data, wf)
#
# with open("json_file.txt", 'r') as rf:
#     data = json.load(rf)
#     print(data)
#     for k in data['people']:
#         print(k)
#         print(k['name'])
#         print(k['from'])
#         print(k['website'])


# ## 10. Write a Python script to merge two Python dictionaries
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'aa': 11, 'bb': 22, 'cc': 33, 'dd': [1,2], 'ee': (3, 4), 'ff': {'p': 100, 'q': 200}}
print({**d1, **d2})


# ## 11. Write a Python program to sum all the items in a dictionary
import functools
print(functools.reduce(lambda x,y : x+y, d1.keys()))

# ## 12. Write a Python program to remove a key from a dictionary. Go to the editor
import copy
d2 = copy.deepcopy(d1)
# d2 = d1
del d2['a']
print(d2)
print(d1)

# ## 13. Write a Python program to map two lists into a dictionary. Go to the editor
a = [11, 2, 3]
b = ['a', 'b', 'c']
print(dict(zip(b, a)))

# ## 14. Write a Python program to sort a dictionary by key. Go to the editor
print(sorted(d1.items(), key=lambda x: x[0]))

# ## 15. Write a Python program to get the maximum and minimum value in a dictionary. Go to the editor
print(max(d1.keys(), key=lambda x:d1[x]))
print(min(d1.keys(), key=lambda x:d1[x]))

# ## 16. Write a Python program to get a dictionary from an object's fields. Go to the editor

# ## 17. Write a Python program to remove duplicates from Dictionary. Go to the editor
student_data = {
    'id1':
        {
            'name': ['Sara'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        },
    'id2':
        {
            'name': ['David'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        },
    'id3':
        {
            'name': ['Sara'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        },
    'id4':
        {
            'name': ['Surya'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        },
}

new_student_list = {}
for i, j in student_data.items():
    if j not in new_student_list.values():
        new_student_list[i] = j
print(new_student_list)

# ## 18. Write a Python program to check a dictionary is empty or not. Go to the editor
test_dict = {}
print(bool(test_dict))
if len(test_dict) == 0:
    print("empty")
else:
    print("Not empty")


# ## 19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


# ## 20. Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},
# {"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
