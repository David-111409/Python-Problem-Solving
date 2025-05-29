'''
Remove Trailing and Leading Zeros
Create a function that takes in a number as a string n and
 returns the number without trailing and leading zeros.

Trailing Zeros are the zeros after a decimal point 
which don't affect the value (e.g. the last three zeros in 3.4000 and 3.04000).
Leading Zeros are the zeros before a whole number which don't affect the value (e.g. 
the first three zeros in 000234 and 000230).

Examples
remove_leading_trailing("230.000") ➞ "230"

remove_leading_trailing("00402") ➞ "402"

remove_leading_trailing("03.1400") ➞ "3.14"

remove_leading_trailing("30") ➞ "30"
====================================================================
Notes
Return a string.
If you get a number with .0 on the end, return the integer value (e.g. return "4" rather than "4.0").
If the number is 0, 0.0, 000, 00.00, etc... return "0".
'''


def remove_leading_trailing(string_num):
    flt = float(string_num)
    
    if flt == int(flt):
        return f"{int(flt)}"
    else :
        return f"{flt}"




print(remove_leading_trailing("230.000") == "230")
print(remove_leading_trailing("00402") == "402")
print(remove_leading_trailing("03.1400") == "3.14")
print(remove_leading_trailing("30") == "30")
print(remove_leading_trailing("30.0000") == "30")
print(remove_leading_trailing("24340") == "24340")
print(remove_leading_trailing("0404040") == "404040")
print(remove_leading_trailing("0") == "0")
print(remove_leading_trailing("00") == "0")
print(remove_leading_trailing("0.000000") == "0")
print(remove_leading_trailing("0000.000") == "0")
print(remove_leading_trailing("00.0001") == "0.0001")
print(remove_leading_trailing("10000") == "10000")
print(remove_leading_trailing("1345") == "1345")
print(remove_leading_trailing("30.000020") == "30.00002")
print(remove_leading_trailing("00200.1900001") == "200.1900001")
