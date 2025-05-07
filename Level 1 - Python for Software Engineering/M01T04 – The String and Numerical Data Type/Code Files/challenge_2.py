"""
Ask the user for a restaurant, number and print.
2025-05-07 EJS
"""

string_fav = input("What is your favorite restaurant? ")
int_fav = int(input("What is your favorite integer? "))

print(f"The user's favorite restaurant is {string_fav}.")
print(f"The user's favorite integer is {int_fav}.")

cast_attempt = int(string_fav)
"""
This does not work because each character in the string is itself an integer.
To convert a whole string (really a sequence of characters) would require 
separate typecastings for each element.
"""