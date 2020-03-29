# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an
# argument, also create a lambda function that multiplies argument x with argument y and print the result.

z = lambda x: x+15
print(z(3))
z1 = lambda x,y: x*y
print(z1(2, 3))

# 2. Write a Python program to create a function that takes one argument, and that argument will be
# multiplied with an unknown given number. Go to the editor
z = lambda x: x*10
print(z(2))

# 3. Write a Python program to sort a list of tuples using Lambda.
print(sorted([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)], key=lambda x:x[1]))

# 4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
print(sorted({'English': 88, 'Science': 90, 'Maths': 97, 'Social sciences': 82}.items(), key=lambda x:x[0][0]))

# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
print(list(filter(lambda x: isinstance(x, int), [1,2,3,'1',41, 'a'])))

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
print(list(map(lambda x: x**3, [1,2,3])))

# 7. Write a Python program to find if a given string starts with a given character using Lambda. Go to the editor
z = lambda x: True if x.startswith('P') else False
print(z("Paru"))

# 8. Write a Python program to extract year, month, date and time using Lambda. Go to the editor


# 9. Write a Python program to check whether a given string is number or not using Lambda. Go to the editor
z = lambda x: True if isinstance(x, str) else False
print(z("ADS"))

# 10. Write a Python program to create Fibonacci series upto n using Lambda.

#
# 11. Write a Python program to find intersection of two given arrays using Lambda. Go to the editor
z = lambda x,y: set(x).intersection(set(y))
print(z([1,2,3,4,5], [2,3,4,5,7,4,2,3,5,7]))

# 12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda. Go to the editor
z = sorted([1,2,-1,-4,5,-3], key=lambda x: x)
print(z)

# 13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda. Go to the editor
list1 = [1,2,3,3,4]
odd_count = len(list(filter(lambda x: x%2 == 0, list1)))
even_count= len(list(filter(lambda x: x%2 !=0, list1)))
print(odd_count, even_count)

# 14. Write a Python program to filter a given list whether the values in the list are having length of 6 using Lambda
lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(list(filter(lambda x: x if len(x) == 6 else '', lst)))


# 15. Write a Python program to add two given lists using map and lambda.
l1 = [1,2,3]
l2 = [4,5,6]
print(list(map(lambda x,y: x+y, l1,l2)))

# 16. Write a Python program to find the second lowest grade of any student(s) from the given names
# and grades of each student using lists and lambda. Input number of students, names and grades of each student.

# 17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda. Go to the editor
# Click me to see the sample solution
#
# 18. Write a Python program to find palindromes in a given list of strings using Lambda. Go to the editor
# Click me to see the sample solution
#
# 19. Write a Python program to find all anagrams of a string in a given list of strings using lambda. Go to the editor