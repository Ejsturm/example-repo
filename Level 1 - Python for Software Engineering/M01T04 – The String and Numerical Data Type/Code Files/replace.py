"""
Use built-in Python string methods to adjust the given string.
2025-05-07 EJS
"""

original_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."
replaced_string = original_string.replace("!", " ", -1)
upper_string = replaced_string.upper()

print(replaced_string)
print(upper_string)
print(upper_string[::-1])