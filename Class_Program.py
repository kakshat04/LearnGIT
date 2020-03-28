"""
3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid
but "[)", "({[)]" and "{{{" are invalid.
"""


class CheckParam:
    def __init__(self, inp_str):
        self.inp_str = inp_str

    def paran_check(self):
        a = 0
        flag = False
        for i in self.inp_str:
            if i in ['(', ')', '{', '}', '[', ']']:
                if a == 0:
                    a = ord(i)
                else:
                    if ord(i) == a:
                        print("Same Parentheses found -- FAIL")
                        a = 0
                        return flag
                    elif abs(a-ord(i)) == 1:
                        # print(a)
                        # print(ord(i))
                        print("Proper round bracket end found -- PASS")
                        a = 0
                        flag = True
                    elif abs(a-ord(i)) == 2:
                        # print(a)
                        # print(ord(i))
                        print("Proper bracket end found -- PASS")
                        a = 0
                        flag = True
                    else:
                        print("Invalid Parentheses Found -- FAIL")
                        # print(a)
                        # print(ord(i))
                        a = 0
                        return flag
        return flag


obj1 = CheckParam("{{{")
print(obj1.paran_check())


"""
4. Write a Python class to get all possible unique subsets from a set of distinct integers
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
"""
class CheckSubSet:
    def sub(self, l):
        l1 = [[]]
        for i in l:
            l1.append([i])
            for j in range(i+1, l[-1]+1):
                l1.append([i,j])
        l1.append(l)
        return l1


obj1 = CheckSubSet()
print(obj1.sub([4,5,6]))


"""
5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum
 equals a specific target number. - Go to the editor
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4
"""
class TestTarget:
    def check_target(self, l1, tar):
        if not isinstance(l1, list):
            return "Enter List"
        if not isinstance(tar, int):
            return "Enter Target in Number"
        for i in range(len(l1)):
            for j in range(i+1, len(l1)):
                if l1[i] + l1[j] != tar:
                    # i += 1
                    break
                else:
                    return i, j

obj1 = TestTarget()
print(obj1.check_target([10,50,20,330,20,20,30], 40))


"""
6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. - Go to the editor
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""
class ThreeSum:
    def get_three_element(self, l1):
        l2 = []
        last = l1[-1]
        new_lst_ngtv = []
        # negative_index_end
        for negative_index_end, value in enumerate(l1):
            if value < 0:
                new_lst_ngtv.append(value)
                index_neg = negative_index_end
            else:
                break
        # print(new_lst_ngtv, index_neg)  # Got index for last negative number

        # check positive value of last list data
        for index, value in enumerate(range(index_neg + 1)):
            if abs(l1[index]) == last:
                index = index
                break
        # print(index) # Got -ve value, before with we have to check only in positive cases

        # This logic is to find group of values greater than negative of last value of list
        for i in range(index+1): # [-25,-10]
            for j in range(index_neg+1, len(l1)):  # [2, 4, 8, 10]
                for k in range(j+1, len(l1)):
                    if l1[i] + l1[j] + l1[k] == 0:
                        l2.append([l1[i], l1[j], l1[k]])

        # This logic is for find group of values smaller than negative of last value of list
        # [-25, -10, -7, -6, -3, 2, 4, 8, 9, 10]
        for i in range(index+1, index_neg+1):
            for j in range(i+1, index_neg + 1):
                for k in range(j + 1, len(l1)):
                    if l1[i] + l1[j] + l1[k] == 0:
                        l2.append([l1[i], l1[j], l1[k]])
        return l2

obj1 = ThreeSum()
# l1 = [-16, -10, -5, -4, -1, 10, 9, 6, 5, 4, 3, 2, 1]
print(obj1.get_three_element([-16, -10, -5, -4, -1, 10, 9, 6, 5, 4, 3, 2, 1]))


"""
8. Write a Python class to reverse a string word by word. - Go to the editor
Input string : 'hello .py'
Expected Output : '.py hello'
"""
class ReverseString:
    def __init__(self, rev):
        self.rev = rev

    def rev_str(self):
        # Covert string to list
        return" ".join(reversed(self.rev.split(" ")))


obj1 = ReverseString('hello .py')
print(obj1.rev_str())


"""
9. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and
 print_String print the string in upper case.
"""
class CheckString:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter String :" )

    def print_string(self):
        print(self.str1.upper())
        # return z.upper()

# obj1 = CheckString()
# obj1.get_string()
# obj1.print_string()


"""
10. Write a Python class named Rectangle constructed by a length and width and a method which will 
compute the area of a rectangle
"""
class Shape:
    def __init__(self, length, breadth):
        self.lenth = length
        self.breadth = breadth


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        return self.lenth * self.breadth


class Object(Shape):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.__height = height

    def area(self):
        return self.lenth * self.breadth*self.__height


obj = Object(5, 10, 20)
print(obj.area())


"""
11. Write a Python class named Circle constructed by a radius and two methods which will
compute the area and the perimeter of a circle.
"""
class Cirle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius**2

    def perimeter(self):
        return 2 * 3.14 * self.__radius


obj_circle = Cirle(5)
print("%.2f " %(obj_circle.area()))
print("%.2f " %(obj_circle.perimeter()))
# print()
# print("%.2f "%per)

"""
12. Write a Python program to get the class name of an instance in Python. 
"""
print(obj_circle.__class__.__name__)
print(issubclass(Rectangle, Shape))
print(isinstance(obj_circle, Cirle))