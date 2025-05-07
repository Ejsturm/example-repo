"""
Obtain the name, age and house address of the user using inputs.
Print the information in a nice, formatted sentence. 2025-05-07 EJS
"""

# Obtain information
user_name = input("What is your name: ")
user_age = input("What is your age: ")
house_num = input("What is your house number: ")
street_name = input("What is your street's name: ")

print(f"This is {user_name}. They are {user_age} years old and they live at house number {house_num} on {street_name}.")