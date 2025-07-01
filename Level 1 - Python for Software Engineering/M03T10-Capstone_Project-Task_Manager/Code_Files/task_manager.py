'''A capstone project at the end of 'Level 1.' Using the template given
as a foundation, modify it to enable users to login with a password,
choose a desired option from a menu, and execute tasks. There are
several subsequent tasks to upgrade the baseline program.

I will use version control along the way. 2025-06-12 EJS'''

# ===== Importing external modules ===========

# Setting up path string to make future code more readable:
MY_PATH = ("c:/Users/sturm/Documents/ES25040017967/Level 1 - Python for "
           "Software Engineering/M03T10-Capstone_Project-Task_Manager/"
           "Code_Files/")

# ==== Login Section ====
# Check to make sure user.txt exist in the right place, open it, and
# store its contents in a dictionary.
try:
    with open(MY_PATH+"user.txt", 'r', encoding="utf-8") as file:
        valid_login_data = {}
        for line in file:
            new_user, new_pw = line.split(",")
            new_user = new_user.strip()
            new_pw = new_pw.strip()
            valid_login_data.update({new_user: new_pw})
except FileNotFoundError:
    print("user.txt does not exist; please check the path and try again.")

# Check user's name and password for authentication.
# First check if the username is valid.
while True:
    user_inp = input("Enter user name: ").strip()
    if user_inp in valid_login_data:
        # Valid username entered; check for corresponding password.
        pw_inp = input("Enter password: ").strip()
        if pw_inp == valid_login_data[user_inp]:
            # Correct password
            break
        else:
            # Incorrect password; start again with username entry.
            print("Incorrect password entered.\n")
            continue
    else:
        # Invalid username entered.
        print("Invalid username entered.")
        continue

# User is now logged in. Begin main menu option loop.
while True:
    menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
Selection: '''
                 ).strip().lower()

    if menu == 'r':
        # Register a new user and their password to user.txt.
        print("Registering a new user.\n")
        new_name = input("New user's name: ").strip()

        # Check to see if the entered user name already exists.
        if new_name in valid_login_data:
            print("That user name already exists, please try again.\n")
            continue

        # Check that the password entries match.
        new_code_1 = input("New password: ").strip()
        new_code_2 = input("Confirm password: ").strip()

        if new_code_1 == new_code_2:
            # The passwords match; add new information to both the 
            # valid_user dictionary and the user.txt file.
            valid_login_data.update({new_name: new_code_1})
            with open(MY_PATH+"user.txt", 'a+', encoding="utf-8") as file:
                file.write("\n"+new_name+","+new_code_1)
        else:
            # The passwords do not match. Return to main menu.
            print("The passwords did not match. Returning to main menu.\n")

    elif menu == 'a':
        # TODO: Implement the following functionality
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not
              complete.
        '''
        pass  # Remove this once you implement the functionality

    elif menu == 'va':
        # TODO: Implement the following functionality
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in
              the PDF
            - It is much easier to read a file using a for loop.'''
        pass  # Remove this once you implement the functionality

    elif menu == 'vm':
        # TODO: Implement the following functionality
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        pass  # Remove this once you implement the functionality

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
