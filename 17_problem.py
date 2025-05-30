
from math import pi

def height_needed(v):
  
    height = 120 * v / pi
    
    return round(height , 2)




print(height_needed(1), 38.2)
print(height_needed(3), 114.59)
print(height_needed(0.5), 19.1)
print(height_needed(10), 381.97)
print(height_needed(5), 190.99)


'''Make a Vessel of Height
A company asks a small-scale manufacturer to 
produce packaging in which they can ship their cooking oil. 
The company also gives the design for how the vessel should look 
(the shaded portion filled in the image below). Depending upon the 
volume of oil to be packaged, the company requires vessels of varying height.

Create a function to determine what the height of the vessel should be,
 depending on the given volume of oil. Return height of the vessel in centimeters, 
 with up to two decimals of precision.

Cone in Cylinder

Examples
height_needed(0.5) ➞ 19.1

height_needed(5) ➞ 190.99

height_needed(10) ➞ 381.97

Notes
Assume the radius (5cm) will stay constant for all different volume vessels.
volume will be given in the unit of litre.'''
