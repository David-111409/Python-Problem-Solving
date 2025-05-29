'''
Finding the Center and Radius of a Circle
The general form of the equation of a circle is x²+y²+ax+by+c=0
 where a, b, and c are constants.

Create a function that takes numbers a, b and c as arguments, 
and returns a list [(x_c, y_c), r] where (x_c, y_c) is the center and r is the radius.

Examples
circle(-4, -6, -12) ➞ [(2, 3), 5]

circle(8, -2, -32) ➞ [(-4, 1), 7]

circle(16, 4, 67) ➞ [(-8, -2), 1]
'''
from math import sqrt

def circle(a, b, c):
    x_c = -a / 2;
    
    y_c = -b / 2;
    
    r = sqrt(pow(x_c, 2) + pow(y_c, 2) - c);
    
    return [(x_c, y_c), r];



print(circle(-4, -6, -12) == [(2, 3), 5])
print(circle(8, -2, -32) == [(-4, 1), 7])
print(circle(16, 4, 67) == [(-8, -2), 1])
print(circle(-2, -2, 1) == [(1, 1), 1])
print(circle(-14, -24, 129) == [(7, 12), 8])
print(circle(6, 14, 49) == [(-3, -7), 3])
print(circle(-10, 28, 121) == [(5, -14), 10])
print(circle(0, 0, -9) == [(0, 0), 3])
