'''This program reads in DOB information from a provided file (DOB.txt), 
extracts information, and then formats the printout. 2025-05-13 EJS'''

import os

try:
    with open("C:/Users/sturm/Documents/Software_Engineering/Level_1/M02T05/Code Files/Input/Task file/DOB.txt", "r") as file:
        # Create storage lists.
        names = []
        birthdays = []
        for line in file:
            # Extract one line at a time.
            split = line.strip().split()

            # Format and store data in appropriate list.
            names.append(" ".join([split[0], split[1]]))
            birthdays.append(" ".join([split[2], split[3], split[4]]))

        print("Name")
        for n in range(len(names)):
            print(names[n])
        
        print("\nBirthdate")
        for b in range(len(birthdays)):
            print(birthdays[b])

except FileNotFoundError:
    print("The file does not exist. Check and try again.")