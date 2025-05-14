'''This program iterative takes in names until the name 'John' is given.
2025-05-13 EJS'''

name = input("Enter your name: ")
wrong_names = []
while (name != "John"):
    wrong_names.append(name)
    name = input("Enter your name: ")

print("Incorrect names:" + str(wrong_names))