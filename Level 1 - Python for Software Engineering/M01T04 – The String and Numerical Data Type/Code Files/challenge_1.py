"""
The user provides triangle side lengths and then fundamental geometry is done.
2025-05-07 EJS
"""
import math

side1 = float(input("Enter triangle side length 1: "))
side2 = float(input("Enter triangle side length 2: "))
side3 = float(input("Enter triangle side length 3: "))

s = (side1 + side2 + side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print("The triangle's area is {:.3f} units square.".format(area))