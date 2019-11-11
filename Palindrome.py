import re


def get_input(text):
    return input(text)

#replace 'get_input("enter text here: ")' with '' to hardcode input for testfile
val = get_input("enter text here: ")


def reverse(val):
    # this is returning a string using ::-1 that returns word backwards
    return val[::-1]

def format(val):
    # enter all formatting information here
    val = re.sub('[^A-Za-z0-9]+', '', val)  # regex to remove all special characters
    val = val.lower()  # change to lower casing
    val = val.replace(" ", "")  # remove spacing
    return val

def isPalindrome(val):
    # this is calling a reversed function
    originalval = val
    val = format(val)
    rev = reverse(val)

    # Checking if both string are equal or not
    if (val == ''):
        print("No value entered")
    elif (val == rev):
        print("'" + originalval + "'" + " is Palindrome")
        return True
    else:
        print("'" + originalval + "'"" is not Palindrome as it becomes ""'" + rev + "'"" backwards" )
        return False

isPalindrome(val)
