"""
Ask the user for a string and then use several built-in subroutines to
manipulate and extract details from it. Print results.
2025-05-07 EJS
"""

str_manip = input("Please provide a sentence (no punctuation at end please): ")

# Find and print string length.
string_length = len(str_manip)
print(f"The string is {string_length} characters long.")

# Identify last letter and replace with "@". Print.
last_letter = str_manip[-1] # The final character is punctuation.
replaced_string = str_manip.replace(last_letter, "@", -1)
print(replaced_string)

# Print the last three characters in backwards order.
print(str_manip[-4:-1:-1])

# The 5-character made up word.
new_word = str_manip[:3] + str_manip[-2:]
print(new_word)