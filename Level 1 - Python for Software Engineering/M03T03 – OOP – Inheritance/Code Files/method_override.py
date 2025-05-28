'''Create a parent and child class with inheritance such that one of
the subroutines in the parent can be overriden by the child.
2025-05-27 EJS'''


class Adult:
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        print(f"{self.name} is {self.age} and they are old enough to drive.")


class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is {self.age} and is too young to drive.")


# Ask the user for their info.
user_name = input("What is your name: ")
user_age = int(input("Waht is your age: "))
user_eye_color = input("What is your eye color: ")
user_hair_color = input("What is your hair color: ")

if (user_age >= 18):
    person_1 = Adult(user_name, user_age, user_eye_color, user_hair_color)
else:
    person_1 = Child(user_name, user_age, user_eye_color, user_hair_color)

person_1.can_drive()
