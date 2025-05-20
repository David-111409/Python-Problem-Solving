


'''
Does a Number Exist?
Create a function which validates whether a given number exists, 
and could represent a real life quantity. Inputs will be given as a string.

Examples
validStrNumber("3.2") ➞ True

validStrNumber("324") ➞ True

validStrNumber("54..4") ➞ False

validStrNumber("number") ➞ False
Notes
Accept numbers such as .5 and 0003.
'''


def validStrNumber(string):
    
    try:
        float(string)
        return True
    
    except ValueError:
        return False
    
    
    
    
print(validStrNumber("3.2"), True)
print(validStrNumber("324"), True)
print(validStrNumber("54..4"), False)
print(validStrNumber("number"), False)
print(validStrNumber(".5"), True)
print(validStrNumber("00003."), True)
print(validStrNumber("3.e"), False)
print(validStrNumber("1234321"), True)
print(validStrNumber(".42.3"), False)
print(validStrNumber("0000000"), True)
print(validStrNumber("000.000"), True)
