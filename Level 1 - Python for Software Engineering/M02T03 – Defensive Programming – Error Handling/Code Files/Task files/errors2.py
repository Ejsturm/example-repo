# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion" # Syntax: add quotes. Logic: made lower case.
animal_type = "cub"
number_of_teeth = 16

# Runtime: in the line below the variables are concatenated in the wrong order.
# Runtime: update the string to be a formatted string such that the variable values would populate
# Logic: added a period at the end.
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."

print(full_spec) # Syntax: added parenthesis.