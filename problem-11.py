"""
Four Points Make a Square

The function is given four points with (x, y) coordinates in no particular order. 
Determine if these points make a square and return True / False.

A square has four equal sides with positive length and four 90-degree angles.

Examples
valid_square((0, 0), (1, 1), (1, 0), (0, 1)) ➞ True

valid_square((0, 0), (1, 1), (1, 0), (0, 12)) ➞ False

valid_square((1, 0), (-1, 0), (0, 1), (0, -1)) ➞ True

valid_square((0, 0), (0, 0), (0, 0), (0, 0)) ➞ False

Notes
A square also has equal diagonals.
"""
from math import sqrt , isclose

def valid_square(first, second, third, fourth):
    x1, y1 = first
    x2, y2 = second
    x3, y3 = third
    x4, y4 = fourth
    
    d1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    d2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    d3 = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
    d4 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)    
    d5 = sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)
    d6 = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    
    sides = sorted([d1, d2, d3, d4, d5, d6])
    
    return sides[0] == sides[1] == sides[2] == sides[3] and all([value > 0 for value in sides]) and isclose(sides[4] ** 2, sides[0] * sides[0] * 2 ) and isclose(sides[4], sides[5])



from time import perf_counter
tic = perf_counter()

print(valid_square((0, 0), (1, 1), (1, 0), (0, 1)), True)
print(valid_square((0, 0), (1, 1), (1, 0), (0, 12)), False)
print(valid_square((1, 0), (-1, 0), (0, 1), (0, -1)), True)
print(valid_square((0, 0), (0, 0), (0, 0), (0, 0)), False)
print(valid_square((0, 4), (4, 6), (3, 3), (1, 7)), True)
print(valid_square((11, 23), (16, 32), (18, 18), (23, 25)), False)
print(valid_square((2, 2), (8, 15), (-11, 8), (-5, 21)), True)
print(valid_square((-16, 20), (-18, 3), (-1, -1), (3, 16)), False)
print(valid_square((-28, 16), (-27, 11), (-22, 17), (-21, 11)), False)
print(valid_square((41, -37), (49, 10), (2, 18), (-6, -29)), True)
print(valid_square((-74, 89), (-28, 71), (-46, 25), (-92, 43)), True)
print(valid_square((23, 36), (1, -36), (45, -14), (-21, 8)), False)
print(valid_square((-29, 88), (-43, 19), (-112, 33), (-98, 102)), True)
print(valid_square((15, 125), (-86, 133), (-31, 179), (-41, 78)), False)
print(valid_square((-149, 115), (-28, 158), (-110, 197), (-67, 76)), True)
print(valid_square((148, 349), (169, 96), (32, 212), (285, 233)), True)
print(valid_square((-84, 19), (56, -48), (-2, -187), (-141, -130)), False)
print(valid_square((77, -133), (42, 164), (207, 34), (-91, -3)), False)
print(valid_square((-922, 84), (-1088, 1061), (55, 250), (-111, 1227)), True)
print(valid_square((53, 2547), (22, 787), (919, 1650), (-840, 1681)), False)
print(valid_square((-1040, 1021), (-1069, 729), (-748, 992), (-777, 700)), True)

print('t_sec = {:.6f}'.format(perf_counter() - tic))
