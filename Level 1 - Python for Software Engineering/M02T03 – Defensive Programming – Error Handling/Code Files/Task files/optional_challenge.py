'''A python program with 2 compilation errors, a runtime error, and a logical
error. 2025-05-12 EJS
'''

import math
a = 1
b = 2 
c = 3
# Once again, let's use the quadratic formula. The correct form:
# For ax^2 + bx + c = 0
# x = [-b +- sqrt(b^2 - 4ac)]/(2a)

# This has 2 syntax errors since math.sqrt was not called correctly.
# The other is that no multiplication was done in the denominator.
positive_x = -1*b + sqrt(b**2 - 4*a*c)/(2a)

# This has a logical error since b should be squared, not cubed.
negative_x = (-1*b - math.sqrt(b**3 - 4*a*c))/(2*a)

# This has a runtime error since the float negative_x was not typecast to a string.
# This also has a syntax error since the p in print is capitalized.
Print("The second root of the linear equation is " + negative_x + ". Tada!")