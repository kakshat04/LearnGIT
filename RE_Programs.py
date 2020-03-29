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


# print(check_num("My phn number is 974   54574 448787as"))


# ## 19. Write a Python program to search some literals strings in a string.  
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
# string where the pattern occurs.  

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


# check_string('The quick brown fox jumps over the lazy dog.')

# ## 21. Write a Python program to find the substrings within a string.  
# Sample text : Python exercises, PHP exercises, C# exercises'
# Pattern :'exercises'
def func_substring(text):
    pattern = "exercises"
    print(re.findall(pattern, text))

# func_substring("Python exercises, PHP exercises, C# exercises")


# ## 22. Write a Python program to find the occurrence and position of the substrings within a string.
def func_substring(text):
    pattern = "Python"
    for match in re.finditer(pattern, text):
        print(match.start())
        print(match.end())
        print(match.group(0))
    # print(z)
#     match = re.search(pattern, text)
#     print(match.start())
#     print(match.end())
#     print(match.string)
#     print(match.group(0))
# func_substring("Python exercises, Python exercises, C# exercises")

# ## 23. Write a Python program to replace whitespaces with an underscore and vice versa.
def replace(text):
    # print(re.sub(r'\s', '_', text)) # and re.sub(r'_', ' ', text))
    t1 = ""
    for i in text:
        print(i, end=' ')
        if i == " ":
            t1 += "_"
        elif i == "_":
            t1 += " "
        else:
            t1 += i
    print(t1)

# replace("kumar Akshat_Srivastava")

# ## 24. Write a Python program to extract year, month and date from a an url
def get_date(url):
    z = re.finditer(r'\d{4}\/\d{1,2}\/\d{1,2}', url)
    for match in z:
        print(match.group())
        print(match.start())
        print(match.end())

# get_date("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-rests-on-one/2016/09/02/")

# ## 25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format
text = "2026-01-02"
pattern = '(19[0-9][0-9]|20[0-9][0-9])(-|.|\/)(0[1-9]|[1-9]|1[0-2])(-|.|\/)(0[1-9]|[1-9]|1[0-9]|2[0-9]|3[0-1])'
print(re.findall(pattern, text))
print(re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', text))
print(re.sub(pattern, '\\5\\4\\3\\2\\1', text))

t1 = "daABCda"
print(re.sub('(A)(B)(C)', "\\1\\2\\3", t1))


# ##26. Write a Python program to match if two words from a list of words starting with letter 'P'
count = 0
for i in ["Paru", "puneet", "pAkshat", "Chotu"]:
    if re.search(r'^P|p\w+', i):
        count += 1
    else:
        pass
if count == 2:
    print("Pass")
else:
    print("Fail")



# ## 27. Write a Python program to separate and print the numbers of a given string.
print(re.findall('\d+', "hjadh23231hajkdhaj244123hajdh5234"))

# ## 28. Write a Python program to find all words starting with 'a' or 'e' in a given string.
text = "kumar akshat elastic fsef aeda"
z = re.split(" ", text)
print(z)
for i in z:
    if re.search("^(a|e)", i):
        print(i, end=' ')
# print(re.findall(r'[ae]\w+', ))

# ## 29. Write a Python program to separate and print the numbers and their position of a given string.
text = "hjadh23231hajkdhaj244123hajdh5234"
z = re.finditer(r"\d+", text)
for match in z:
    print([match.group(), match.start(), match.end()])

# ## 30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string
print(re.sub("Road", "rd", "My Road number is Road11"))

# ## Write a Python program to replace all occurrences of space, comma, or dot with a colon
print(re.subn("\s|,|\.", ';', "hjadh haj,kdhaj244. ,123hajdh5234"))


# ## Write a regular expression that will accept an email id. Use the re module.
pattern = r'[A-Za-z0-9.]+@\w+\.com'
print(re.search(pattern, "My email id is dsd51.dsd5@gmail.com").group())