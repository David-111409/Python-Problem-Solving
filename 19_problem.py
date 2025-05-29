def opposite_house(house, n):
    return (2 * n + 1) - house


print(opposite_house(1, 3), 6)
print(opposite_house(3, 3), 4)
print(opposite_house(2, 3), 5)
print(opposite_house(3, 5), 8)
print(opposite_house(7, 11), 16)
print(opposite_house(10, 22), 35)
print(opposite_house(20, 3400), 6781)
print(opposite_house(9, 26), 44)
print(opposite_house(20, 10), 1) 
print(opposite_house(23633656673, 310027696726) == 596421736780)


'''Opposite House 🏘️
Mubashir was walking through a straight street with exactly n identical houses on both sides. 
House numbers in the street look like this:

1 |   | 6

3 |   | 4

5 |   | 2
He noticed that Even numbered houses increase on the right while Odd numbered houses decrease on the left.

Create a function that takes a house number house and length of the street n and 
returns the house number on the opposite side.

Examples
opposite_house(1, 3) ➞ 6

opposite_house(2, 3) ➞ 5

opposite_house(3, 5) ➞ 8
'''
