"""
Does the Triangle Fit into the Triangular Hole?

Create a function that takes the dimensions of two triangles
(as lists) and checks if the first triangle fits into the second one.

Examples
does_triangle_fit([1, 1, 1], [1, 1, 1]) ➞ True

does_triangle_fit([1, 1, 1], [2, 2, 2]) ➞ True

does_triangle_fit([1, 2, 3], [1, 2, 2]) ➞ False

does_triangle_fit([1, 2, 4], [1, 2, 6]) ➞ False
Notes
Triangle fits if it has the same or smaller size as the hole.
The function should return False if the triangle with that dimensions is not possible.
"""
from math import sqrt

def does_triangle_fit(triangle1, triangle2):
    
    [a1, b1, c1] = sorted(triangle1)
    [a2, b2, c2] = sorted(triangle2)
    
    
    if  not (a1 + b1 > c1 and a2 + b2 > c2):
        return False
    
    s1 = (a1 + b1 + c1) / 2
    area1 = sqrt(s1 * (s1- a1) * (s1 - b1) * (s1 - c1))
    
    s2 = (a2 + b2 + c2) / 2
    area2 = sqrt(s2 * (s2- a2) * (s2 - b2) * (s2 - c2))
    
    return area1 <= area2
    
    
    
    
print(does_triangle_fit([1, 1, 1], [1, 1, 1]), True, "Same triangle")
print(does_triangle_fit([1, 1, 1], [2, 2, 2]), True, "Smaller triangle")
print(does_triangle_fit([1, 6, 8], [1, 6, 8]), False, "Not a triangle")
print(does_triangle_fit([12, 63, 42], [1, 6, 8]), False, "too small hole")
print(does_triangle_fit([3, 6, 8], [23, 63, 42]), True, "Hole is too big")
print(does_triangle_fit([3, 6, 8], [1, 10, 8]), False, "impossible hole")
