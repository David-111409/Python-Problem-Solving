def root_digit(num):
    if num < 10: return num
    return root_digit(sum(int(digit) for digit in str(num)))




print(root_digit(12))
print(root_digit(999888777), 9)
print(root_digit(1111177999888777999888777999888777), 1)
print(root_digit(1238763636555555555555), 6)
print(root_digit(1238222222222222222263612387636361238763636), 7)
print(root_digit(0), 0)


"""
Digits Sum Root
Create a function that takes a number and returns one digit that is the result 
of summing all the digits of the input number. When the sum of the digits consists of more than one digit,
 repeat summing until you get one digit.

Examples
root_digit(123) ➞ 6
# 1 + 2 + 3 = 6

root_digit(999888777) ➞ 9

root_digit(1238763636555555555555) ➞ 6
Notes
Recursion is allowed.
"""
