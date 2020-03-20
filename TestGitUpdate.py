def capital(text):
    return text.upper()


def make_changes(func, text1):
    """
    Passing function as parameter
    :param func:
    :param text1:
    :return:
    """
    if text1.isupper():
        return text1
    else:
        return func(text1)


print(capital("abc"))
print(makeChanges(capital, "Bxx"))