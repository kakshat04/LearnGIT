# sort
l1 = [123,23,51,451,415,1234,15124,1]
for i in range(0, len(l1)):
    for j in range(0, len(l1) - 1):
        if l1[j] > l1[j+1]:
            l1[j],  l1[j+1] = l1[j+1], l1[j]
print(l1)
# l1.sort(reverse=True)  # In sort, original list is modified
z = sorted(l1, reverse=True)
print(l1)
print(z)


l = []
for i in "get":
    for j in "set":
        if i is not 't' and j is not 'e':
            l.append(i+j)
print(l)

z = [x+y for x in 'get' for y in 'set' if x is not 't' and y is not 'e']
print(z)


# print odd months using list comprehension
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
z = [months[x] for x in range(0, len(months), 2)]
z1 = [j for i, j in enumerate(months) if i%2 == 0]
print(z)
print(z1)


# Palindrome -- hannah
def palindrome(user_input):
    rev_inp = ""
    for inp in range(len(str(user_input))-1, -1, -1):
        rev_inp += str(user_input)[inp]
    if rev_inp == str(user_input):
        return "Palindrome"
    return "Not Palindrome"


print(palindrome(100))


# Fibonacci -- 112358132134
def fib(inp):
    a = 0
    b = 1
    count = 0
    series = ""
    while count < inp:
        series += str(a)
        c = a + b
        a = b
        b = c
        count += 1
    return series


print(fib(5))


# Prime
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    else:
        return "Prime"


print(check_prime(2))

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    print(ls)
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum)


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
# list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)


a = [1, 2, 3, 4, 5, 6, 7]
l1 = []
for i in a:
    if i == 2 or i == 4:
        continue
    l1.append(i)
print(l1)


class Human:
    profession = "Engineer"

    def __init__(self, profession):
        self.profession = profession

    def get_profession(self):
        print(Human.profession)
        print(self.profession)


obj1 = Human("Doctor")
obj1.get_profession()
print(obj1.profession)



names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    print(ls)
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum)


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
# list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)


a = [1, 2, 3, 4, 5, 6, 7]
l1 = []
for i in a:
    if i == 2 or i == 4:
        continue
    l1.append(i)
print(l1)


class Human:
    profession = "Engineer"

    def __init__(self, profession):
        self.profession = profession

    def get_profession(self):
        print(Human.profession)
        print(self.profession)


obj1 = Human("Doctor")
obj1.get_profession()
print(obj1.profession)


#  Palindrome of a Number
n = 151
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
print(n)
print(rev)
# if


"""
35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
Click me to see the sample solution
"""
class ListModification:
    def __init__(self, lst, num):
        self.lst = lst
        self.num = num

    def lst_mod(self):
        new_lst = []
        for i in range(len(self.lst)):
            for j in range(1, self.num + 1):
                new_lst.append(self.lst[i] + str(j))
        return new_lst

obj1 = ListModification(['p', 'q'], 5)
print(obj1.lst_mod())

"""
49. Write a Python program to convert list to list of dictionaries. Go to the editor
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
 {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
"""

color_name_lst = ["Black", "Red", "Maroon", "Yellow"]
color_code_lst = ["#000000", "#FF0000", "#800000", "#FFFF00"]
dict1 = {}
l1 = []
z = [{'col': a, 'code': b} for a, b in zip(color_name_lst, color_code_lst)]
print(z)


"""
50. Write a Python program to sort a list of nested dictionaries. Go to the editor
Click me to see the sample solution
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
"""
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
z = sorted(my_list, key=lambda e: e['key']['subkey'], reverse=True)

my_dict = {'a': 2, 'd': 5, 'g': 3, 'y': 4}
k = sorted(my_dict.items(), key=lambda x : x[1])

my_dict1 = {'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}
m = sorted(my_dict1, key=lambda x : x['key']['subkey'])

print(m)
print(k)
print(z)


"""
2 arrays as input [3,5,7,9,12], [3, 7, 9, 12]
Output --> 5 - Missing Element in list 1
"""
def find_missing(arr1, arr2):
    missing = " "
    for i in arr1:
        if i not in arr2:
            missing = str(i) + ", " + missing
    return missing


def find_missing_option2(arr1, arr2):
    return list(set(arr1).difference(set(arr2)))

print(find_missing([3,5,7,9,12], [3, 9, 12]))
print(find_missing_option2([3,5,7,9,12], [3, 9, 12]))