'''This program will take names and IDs for subsequent saving. 
2025-05-13 EJS'''

import os

number = int(input("How many students will be registering? "))
student_info = []

for _ in range(number):
    id_number = int(input("Student ID number: "))
    line = f"{id_number}\t______________________________\n"
    student_info.append(line)

with open("reg_form.txt", "w+") as file:
    for i in range(number):
        file.write(student_info[i])