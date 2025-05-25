"""
Is It a Right-Angled Triangle?
Find out if a right-angled triangle can be made given some facts about the shape.

Given varying information about a shape, create a function 
that returns True if the shape could be a right-angle triangle and False if not.
You will be given a list of numbers and a string stating whether the numbers are angles or sides.
The information may indicate more than one possible shape, 
but we just need to know if these details could be found in a right-angled triangle.

Examples
is_right_angle([30, 60], "angle") ➞ True
# A third angle could be 90

is_right_angle([20, 20, 20, 20], "angle") ➞ False
# More than 3 sides

is_right_angle([4, 5, 3], "side") ➞ True
# 3**2 + 4**2 = 5**2

is_right_angle([4, 5], "side") ➞ True
# Third side may be 3

"""
from math import sqrt, isclose

def is_right_angle(ar, string):
    n =  len(ar)
    if n <= 1:
        return True
    elif n > 3:
        return False
    
    elif string == 'angle':
        s = sum(ar)
        if n == 3 and any((a == 90 for a in ar)) and s == 180:
            return True
        elif n == 2:
            if 180 - s == 90:
                return True
              
    elif string == 'side':
        if n == 3:
            ar = sorted(ar)
            if isclose(ar[0] **2 + ar[1] ** 2, ar[2] ** 2)   and ar[0] + ar[1] > ar[2]:
                return True
        if n == 2 and all((j > 0 for j in ar)):
            return True
        
    
    return False
             
    

print(is_right_angle([30, 60], "angle"), True, "Third angle may be 90")
print(is_right_angle([30, 60, 90], "angle"), True, "An angle is 90 and adds to 180")
print(is_right_angle([90], "angle"), True, "An angle is 90")
print(is_right_angle([90, 90, 90], "angle"), False, "More than 180")
print(is_right_angle([20, 20, 20, 20], "angle"), False, "More than 3 sides")
print(is_right_angle([], "angle"), True, "No information, so it could be a right-angled triangle")
print(is_right_angle([90, 90], "angle"), False, "3rd angle will go over 180")
print(is_right_angle([45, 46], "angle"), False, "3rd angle must be 89")
print(is_right_angle([45, 46], "side"), True, "3rd side could be 64.3506")
print(is_right_angle([4, 5, 6], "side"), False, "Does not calculate correctly")
print(is_right_angle([], "side"), True, "No information, so it could be a right-angled triangle")
print(is_right_angle([3, 4, 5], "side"), True, "Calculates correctly")
print(is_right_angle([60, 60, 60], "angle"), False)
print(is_right_angle([177, 2, 1], "angle"), False)
print(is_right_angle([20, 20, 20, 20], "side"), False)
print(is_right_angle([43], "angle"), True)
