import re
# >>> isinstance(10,int)
# True
# >>> isinstance(10,str)
# False
# >>> isinstance('10',str)
# True
# >>> tup = (1, 2, 3)
# >>> a, b, c = tup
# >>> a
# 1
# >>> b
# 2
# >>> c
# 3
# >>> import re
# >>> re.match(r'a[bcd]*b', 'abcbd')
# <re.Match object; span=(0, 4), match='abcb'>
# >>>
# >>>
# >>> print(re.match(r'a[bcd]*b', 'abcbd'))
# <re.Match object; span=(0, 4), match='abcb'>
# >>> print(re.search(r'a[bcd]*b', 'abcbd'))
# <re.Match object; span=(0, 4), match='abcb'>
# >>>
# >>>
# >>> print(re.find(r'a[bcd]*b', 'abcbd'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 're' has no attribute 'find'
# >>>
# >>> print(re.findall(r'a[bcd]*b', 'abcbd'))
# ['abcb']
# >>> print(re.findall(r'a[bcd]b', 'abcbd'))
# []
# >>> print(re.findall(r'a[bcd]b', 'abcb'))
# []
# >>> print(re.findall(r'a[bcd]b', 'abb'))
# ['abb']
# >>> print(re.findall(r'a[bcd]b', 'acb'))
# ['acb']
# >>> print(re.findall(r'a[bcd]b', 'abcb'))
# []
# >>> print(re.findall(r'a[bcd]b', 'abc'))
# []
# >>> print(re.findall(r'a[bcd]*b', 'abcbcbcbd_bcbcdd'))
# ['abcbcbcb']
# >>> print(re.findall(r'a[bcd]*b', 'abcbcbcbb_bcbcdd'))
# ['abcbcbcbb']
# >>> print(re.findall(r'a[bcd]*b', 'abcbcbcbbbcbcdd'))
# ['abcbcbcbbbcb']
# >>> print(re.findall(r'a[bcd]*b', 'abcd'))
# ['ab']
# >>> print(re.findall(r'a[bcd]*b', 'acd'))
# []
# >>> print(re.findall(r'a[bcd]*b', 'a'))
# []
# >>> print(re.findall(r'a[bcd]*b', 'ab'))
# ['ab']
# >>>
# >>>
# >>>
# >>> print(re.findall(r'ca+t', 'cat'))
# ['cat']
# >>> print(re.findall(r'ct', 'cat'))
# []
# >>> print(re.findall(r'cat', 'cat'))
# ['cat']
# >>> print(re.findall(r'ca+', 'cat'))
# ['ca']
# >>> print(re.findall(r'ca*t', 'ct'))
# ['ct']
# >>> print(re.findall(r'ca+', 'cat'))
# ['ca']
# >>> print(re.findall(r'ca*t', 'c'))
# []
# >>> print(re.findall(r'ca*t', 'c'))
# []
# >>>
# >>>
# >>>
# >>>
# >>> print(re.findall(r'ca?t', 'c'))
# []
# >>> print(re.findall(r'ca?t', 'ct'))
# ['ct']
# >>> print(re.findall(r'ca?t', 'cat'))
# ['cat']
# >>> print(re.findall(r'ca?t', 'caat'))
# []
# >>> print(re.findall(r'ca?t', 'cat'))
# ['cat']
# >>>
# >>>
# >>> print(re.findall(r'ca{1,3}t', 'cat'))
# ['cat']
# >>> print(re.findall(r'ca{1,3}t', 'caat'))
# ['caat']
# >>> print(re.findall(r'ca{1,3}t', 'caaat'))
# ['caaat']
# >>> print(re.findall(r'ca{1,3}t', 'caaaat'))
# []
# >>> print(re.findall(r'a/{1,3}b', 'caaaat'))
# []
# >>> print(re.findall(r'a/{1,3}b', 'ab'))
# []
# >>> print(re.findall(r'a/{0,3}b', 'ab'))
# ['ab']
# >>> print(re.findall(r'a/{0,3}b', 'a/b'))
# ['a/b']
# >>> print(re.findall(r'a/{0,3}b', 'a//b'))
# ['a//b']
# >>> print(re.findall(r'a/{0,3}b', 'a///b'))
# ['a///b']
# >>> print(re.findall(r'a/{0,3}b', 'a////b'))
# []
# >>> print(re.findall(r'a/{0,}b', 'a////b'))
# ['a////b']
# >>> print(re.findall(r'a/{0,}b', 'ab'))
# ['ab']
# >>> print(re.findall(r'a/{1,}b', 'ab'))
# []
# >>> print(re.findall(r'a/{1,}b', 'a/b'))
# ['a/b']
# >>> print(re.findall(r'a/{1,}b', 'a//b'))
# ['a//b']
# >>> print(re.findall(r'a/{0,1}b', 'a//b'))
# []
# >>> print(re.findall(r'a/{0,1}b', 'a/b'))
# ['a/b']
# >>> print(re.findall(r'a/?b', 'a/b'))
# ['a/b']
# >>> print(re.findall(r'a/?b', 'a//b'))
# []
# >>> print(re.findall(r'a/?b', 'ab'))
# ['ab']
# >>> print(re.findall(r'^ca?t', 'cat'))
# ['cat']
# >>> print(re.findall(r'^ca?t', 'bcat'))
# []
# >>> print(re.findall(r'ca?t', 'bcat'))
# ['cat']
# >>> print(re.findall(r'^ca?t$', 'bcat'))

strng = 'asdasdad10.12.15dassd,25.12sdsada151.12sdad12.12'
z = re.search(r'\d{1,3}\.\d{1,3}', strng)
# print(z)
if z:
    print(z.span())
else:
    print(z)
z = re.split(r'as', strng, 6)
print(z)

z = re.subn(r'\d{1,3}\.\d{1,3}', '$$$$$$$', strng)
print(z)


