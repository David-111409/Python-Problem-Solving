'''
Finding the Missing Sides of a Right Triangle
Consider a right triangle. Its area and hypotenuse are known.

Create a function that returns the two missing sides. 
The first input is the area and the second input is the hypotenuse. 
Return your answer as a list (the shorter side first). 
If there is no such right triangle, 
return "Does not exist".

Examples
f(3, 6) ➞ [1.015, 5.914]

f(30, 12) ➞ [5.675, 10.574]

f(30, 10) ➞ "Does not exist"

Notes
Round your answer to three decimal places.
'''
from math import sqrt

def f(area, c):
    s = sqrt(c ** 2 + 4 * area)
    d = s ** 2 - 8 * area
    
    if d < 0 or area <=  0 or c <= 0:
        return "Does not exist"
    
    a = (s + sqrt(d)) / 2
    b = (s - sqrt(d)) / 2
    
    a = round(a, 3)
    b = round(b, 3)
    
    return sorted([a, b])

    


print(f(3,6), [1.015, 5.914])
print(f(30,12), [5.675, 10.574])
print(f(30,10), "Does not exist")
print(f(12, 21))
