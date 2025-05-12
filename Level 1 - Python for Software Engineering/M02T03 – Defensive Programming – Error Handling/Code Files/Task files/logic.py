'''This is an example of a logic error in python. 2025-05-12 EJS'''

import math

# This *should* be the quadratic formula.
# Given the standard form of a quadratic polynomial: ax^2 + bx + c = 0
# The correct one: x = [-b +- sqrt(b^2 -4ac)]/(2a)

a = 1
b = 2
c = 1

# Bad logic for the positive root:
positive_x = b + math.sqrt(b**2 -4*a*c)/(2*a)
# There should be parenthesis around the full numerator like this and the first term should be negated like so:
# positive_x = (-1*b + math.sqrt(b**2 -4*a*c))/(2*a)

# Bad logic for the negative root:
# This one is missing the call for the square root, and without parenthesis the desired order of operations will 
# not be followed; the strict interpretation of them will be, so for example the "denominator" factor of 'a' will 
# be in the numerator, not the demoninator.
# Also, b should be squared, not cubed.
negative_x = -1*b + (b**3 - 4*a*c)/2*a