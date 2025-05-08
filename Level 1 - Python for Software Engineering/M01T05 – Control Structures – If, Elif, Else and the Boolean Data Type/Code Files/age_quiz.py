"""
This program asks a user for their age and then prints out one of several
responses based on the age provided based on the if-elif-else logic.
2025-05-08 EJS
"""

user_age = int(input("Please enter your age: "))

if user_age >= 100:
    print("Sorry, you're dead.")
elif user_age >= 65:
    print("Enjoy your retirement.")
elif user_age >= 40:
    print("You're over the hill.")
elif user_age < 13:
    print("You qualify for the kiddie discount.")
elif user_age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")