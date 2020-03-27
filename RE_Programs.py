import re


# #### 1. Write a Python program to check that a string contains only a certain set of character
def text_match(text):
    patterns = r'^\w*$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# ### 2. Write a Python program that matches a string that has an 'a' followed by zero or more b's
def text_match(text):
    patterns = r'ab*'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# ### 3. Write a Python program that matches a string that has an a followed by one or more b's
def text_match(text):
    patterns = r'ab+'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# ### 4. Write a Python program that matches a string that has an a followed by zero or one 'b'
def text_match(text):
    patterns = r'ab?'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# ## 5. Write a Python program that matches a string that has an a followed by three 'b'
def text_match(text):
    patterns = r'ab{3}'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("ab"))
# print(text_match("abb"))
# print(text_match("abbb"))
# print(text_match("abbbb"))
# print(text_match("avbbb"))

# ## 6. Write a Python program that matches a string that has an a followed by two to three 'b'
def text_match(text):
    patterns = r'ab{2,3}'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("ab"))
# print(text_match("abb"))
# print(text_match("abbb"))
# print(text_match("abbbb"))
# print(text_match("avbbb"))


# ## 7. Write a Python program to find sequences of lowercase letters joined with a underscore
def text_match(text):
    patterns = r'[a-z]_[a-z]'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("a_b"))
# print(text_match("ab_b"))
# print(text_match("aB_bb"))
# print(text_match("ab_Bbb"))
# print(text_match("A_BBC_c_d"))


# ## 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def text_match(text):
    patterns = r'[A-Z][a-z]+'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("U_l"))
# print(text_match("Ab_b"))
# print(text_match("aB_bb"))
# print(text_match("ab_bBb"))
# print(text_match("A_BcC_c_d"))


# ## 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def text_match(text):
    patterns = r'a.+b$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("ab"))
# print(text_match("abb"))
# print(text_match("accb"))
# print(text_match("kuabdhkahfjgjkfhu834748924%&&%*&*bjkald"))
# print(text_match("A_BcC_c_d"))


# ## 10. Write a Python program that matches a word at the beginning of a string
def text_match(text):
    patterns = r'^a\w+'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("ab"))
# print(text_match("abb"))
# print(text_match("accb"))
# print(text_match("kuabdhkahfjgjkfhu834748924%&&%*&*bjkald"))
# print(text_match("A_BcC_c_d"))

# ## 11. Write a Python program that matches a word at the end of string, with optional punctuation
def text_match(text):
    patterns = r'\w+$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("The quick brown fox jumps over the lazy dog"))
# print(text_match("abb"))

# ## 12. Write a Python program that matches a word containing 'z'.  ---> wrong
def text_match(text):
    patterns = r'\w*z\w*'
    z = re.search(patterns,  text)
    # if re.search(patterns,  text):
    if z:
        return 'Found a match!', z.group(0)
    else:
        return 'Not matched!'


# print(text_match("The quick brown fox jumps over the lazy dog."))
# print(text_match("abz"))

# ## 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
def text_match(text):
    patterns = r'\Bz\B'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


print(text_match("The quick brown fox jumps over the zly dog."))


# ## 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, & underscores
def text_match(text):
    patterns = r'^[A-Za-z0-9_]*$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match("The quick brown fox jumps over the lyz dog."))
# print(text_match("abb56"))


# ## 15. Write a Python program where a string will start with a specific number.
def text_match(text):
    patterns = r'^7\w*'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'


# print(text_match('7-2345861'))
# print(text_match('6-2345861'))


# ## 16. Write a Python program to remove leading zeros from an IP address
def correct_ip(text):
    pattern = r'\.0+'
    z = re.sub(pattern, ".", text)
    return z


# print(correct_ip("My IP address is 10.0000015.015.15"))


# ## 17. Write a Python program to check for a number at the end of a string
def check_number(text):
    pattern = r'\w*\d$'
    if re.search(pattern, text):
        return "Pattern Match", re.search(pattern, text).group()
    else:
        return "Pattern not match"


# print(check_number("My IP address is 10.0000015.015.15"))


# ## 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
def check_num(text):
    pattern = r'\s\d{1,3}\s'
    if re.search(pattern, text):
        return "Pattern Match", re.search(pattern, text).group()
    else:
        return "Pattern not match"


print(check_num("My phn number is 974   54574 448787as"))


# ## 19. Write a Python program to search some literals strings in a string. Go to the editor
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
def check_string(text):
    patterns = ['fox', 'dog', 'horse']
    for pat in patterns:
        z = re.search(pat, text)
        if z:
            print("Found", pat)
        else:
            print("Not Found", pat)


# check_string('The quick brown fox jumps over the lazy dog.')


# ## 20 Write a Python program to search a literals string in a string and also find the location within the original
# string where the pattern occurs. Go to the editor

# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'

def check_string(text):
    patterns = ['fox', 'dog', 'horse']
    for pat in patterns:
        z = re.search(pat, text)
        if z:
            print("Found", z.group(), z.start(), z.end())
        else:
            print("Not Found", pat)


check_string('The quick brown fox jumps over the lazy dog.')