# Microsoft Windows [Version 10.0.18362.720]
# (c) 2019 Microsoft Corporation. All rights reserved.
#
# C:\Users\ADMIN>python
# Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# >>>
# >>> for i,j in enumerate(['jan',feb','mar']):
#   File "<stdin>", line 1
#     for i,j in enumerate(['jan',feb','mar']):
#                                      ^
# SyntaxError: invalid syntax
# >>> months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>> for i,j in enumberate(months):
# ...     print(i,j)
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'enumberate' is not defined
# >>>
# >>>
# >>>
# >>> for i,j in enumerate(months):
# ...     print(i,j)
# ...
# 0 jan
# 1 feb
# 2 mar
# 3 apr
# 4 may
# 5 jun
# 6 jul
# 7 aug
# 8 sep
# 9 oct
# 10 nov
# 11 dec
# >>>
# >>>
# >>>
# >>> iter(months)
# <list_iterator object at 0x0000021AB2658F88>
# >>> z = iter(months)
# >>> z.next()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list_iterator' object has no attribute 'next'
# >>> months
# ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> months.insert(2,10)
# >>> months
# ['jan', 'feb', 10, 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>> months[2] = "Aksjay"
# >>> months
# ['jan', 'feb', 'Aksjay', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>> del months[2]
# >>> months
# ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>>
# >>>
# >>> months.remove("mar")
# >>> months
# ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>> z = months.remove("mar")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
# >>>
# >>>
# >>>
# >>>
# >>> months.insert(2, 'mar')
# >>> months
# ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>> z = months.remove("mar")
# >>> z
# >>> z
# >>> months
# ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# >>> months.insert(2, 'mar')
# >>>
# >>>
# >>>
# >>>
# >>> z = months.pop("mar")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object cannot be interpreted as an integer
# >>> z = months.pop(2)
# >>> z
# 'mar'
# >>> z = months.pop()
# >>> z
# 'dec'
# >>> months
# ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov']
# >>> months.index('apr')
# 2
# >>> months.sort()
# >>> months
# ['apr', 'aug', 'feb', 'jan', 'jul', 'jun', 'may', 'nov', 'oct', 'sep']
# >>> months
# ['apr', 'aug', 'feb', 'jan', 'jul', 'jun', 'may', 'nov', 'oct', 'sep']
# >>> months = ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov']
# >>>
# >>>
# >>>
# >>>
# >>> months
# ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov']
# >>> z = sorted(months)
# >>> z
# ['apr', 'aug', 'feb', 'jan', 'jul', 'jun', 'may', 'nov', 'oct', 'sep']
# >>> months
# ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov']
# >>>
# >>>
# >>>
# >>> z = sorted(months, reverse=True)
# >>> z
# ['sep', 'oct', 'nov', 'may', 'jun', 'jul', 'jan', 'feb', 'aug', 'apr']
# >>> weeks = ['mon', 'tue', 'wed', 'thru', 'fri', 'sat', 'sun']
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> months.extend(weeks)
# >>> months
# ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'mon', 'tue', 'wed', 'thru', 'fri', 'sat', 'sun']
# >>> l1 = [10, 'a', 1.1, ('a','b'), [1,2], {'a': 1, 'b' : 2}]
# >>> l1
# [10, 'a', 1.1, ('a', 'b'), [1, 2], {'a': 1, 'b': 2}]
# >>> type(l1[-1])
# <class 'dict'>
# >>> type(l1[-2])
# <class 'list'>
# >>> type(l1[3])
# <class 'tuple'>