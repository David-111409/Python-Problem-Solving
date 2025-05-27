
digits = "0123456789abcdef"

def integer_to_string(num, base):
   
       if num < base: return digits[num]
        
       return integer_to_string(num // base, base) + digits[num % base]
    



print(integer_to_string(0, 2))
print(integer_to_string(10, 2))
print(integer_to_string(10, 2), "1010")
print(integer_to_string(1642, 8), "3152")
print(integer_to_string(102, 2), "1100110")
print(integer_to_string(212, 16), "d4")
print(integer_to_string(18, 2), "10010")
print(integer_to_string(3162, 16), "c5a")
print(integer_to_string(10, 8), "12")
print(integer_to_string(162, 8), "242")
print(integer_to_string(27, 2), "11011")
print(integer_to_string(4321, 16), "10e1")
print(integer_to_string(1622, 16), "656")


'''
Positive Integer Into Base 2, 8 and 16
Create a function that takes a positive integer number 
(one of base2, base8, or base16) and converts the integer into the given base 
and returns a string using recursion.

Examples

integer_to_string(10 , 2) ➞ "1010"
# Base = 2

integer_to_string(1642 , 8) ➞ "3152"
# Base = 8

integer_to_string(212 , 16) ➞ "d4"
# Base = 16

Notes
Input is a positive integer and base = 2, 8, or 16.
Please use recursion to solve this.
'''
