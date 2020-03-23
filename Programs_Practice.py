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


