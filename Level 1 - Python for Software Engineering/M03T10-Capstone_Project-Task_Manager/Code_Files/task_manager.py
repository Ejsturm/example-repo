'''Update: modifying code to accomplish tasks 2 and 3. 2025-07-02 EJS

A capstone project at the end of 'Level 1.' Using the template given
as a foundation, modify it to enable users to login with a password,
choose a desired option from a menu, and execute tasks. There are
several subsequent tasks to upgrade the baseline program.

I will use version control along the way. 2025-06-12 EJS'''

# ===== Importing external modules ===========
from datetime import date

# Setting up path string to make future code more readable:
MY_PATH = ("c:/Users/sturm/Documents/ES25040017967/Level 1 - Python for "
           "Software Engineering/M03T10-Capstone_Project-Task_Manager/"
           "Code_Files/")

# ====== Subroutines ===================================================


def reg_user():
    '''Only for admin use. Adds a new user to the user.txt file after
    checking to ensure that the user does not already exist.'''

    new_user = input("New user's name: ").strip()
    if new_user in valid_login_data:
        print("That user name already exists, please try again.\n")
        return
    else:
        # Check that the password entries match.
        new_code_1 = input("New password: ").strip()
        new_code_2 = input("Confirm password: ").strip()

        if new_code_1 == new_code_2:
            # The passwords match; add new information to both the
            # valid_user dictionary and the user.txt file.
            valid_login_data.update({new_user: new_code_1})
            with open(MY_PATH+"user.txt", 'a+', encoding="utf-8") as file:
                file.write("\n"+new_user+","+new_code_1)
        else:
            # The passwords do not match. Return to main menu.
            print("The passwords did not match. Returning to main menu.\n")
    return


def add_task():
    '''Enable any present user to add a task to the tasks.txt file.
    Prompt user for relevant information.'''

    task_username = input("Username for task assignment: ").strip()
    # Check to ensure the user exists.
    if task_username not in valid_login_data:
        print("That username doesn't exist, please try again.\n")
        return

    # Get other task data.
    task_name = input("Task title: ").strip()
    description = input("Provide a brief description: ").strip()
    due_date = input("Provide a due date (DD Mon YYYY): ").strip()

    # Get current date information and reformat it apporpiately.
    # Used geeksforgeeks.org to find the datetime module.
    curr_year, curr_month_num, curr_day = str(date.today()).split("-")
    months = {"01": "Jan",
              "02": "Feb",
              "03": "Mar",
              "04": "Apr",
              "05": "May",
              "06": "Jun",
              "07": "Jul",
              "08": "Aug",
              "09": "Sep",
              "10": "Oct",
              "11": "Nov",
              "12": "Dec"}
    current_month = months[curr_month_num]
    current_date = " ".join([curr_day, current_month, curr_year])

    # Format the new task's string.
    full_task_string = ", ".join([task_username, task_name, description,
                                 current_date, due_date, "No"])

    # Add the new task string to the task file.
    with open(MY_PATH+"tasks.txt", 'a+', encoding="utf-8") as file:
        file.write("\n"+full_task_string)


def print_task(line):
    '''Will print a nicely formatted version for a single task.

    Parameters:
    line (string): the line of data with all task information
    '''

    contents = line.split(", ")
    print(f"{'Task:': <20}{contents[1]}")
    print(f"{'Assigned to:': <20}{contents[0]}")
    print(f"{'Date assigned:': <20}{contents[3]}")
    print(f"{'Due date:': <20}{contents[4]}")
    print(f"{'Task complete?': <20}{contents[5].strip()}")
    print(f"Task description:\n  {contents[2]}")
    print("-"*80)


def view_all():
    '''Prints all tasks by calling the print_task() subroutine for
    formatting.'''

    total_tasks = 0

    print("-"*80)
    with open(MY_PATH+"tasks.txt", "r", encoding="utf-8") as file:
        for line in file:
            print_task(line)
            total_tasks += 1
    print(f"There are {total_tasks} tasks in total.\n")


def view_mine(user):
    '''Prints tasks only associated with the current_user. Uses the
    print_task() subroutine for formatting.

    Parameters:
    user (string): the current username
    '''

    total_tasks = 0

    print("-"*80)
    with open(MY_PATH+"tasks.txt", "r", encoding="utf-8") as file:
        for line in file:
            contents = line.split(", ")
            # Check task's assinged person.
            if contents[0].strip() == user:
                total_tasks += 1
                print_task(line)
    print(f"The user {user} has {total_tasks} assigned to them.\n")


def view_completed():
    '''Only for admin use. Shows all tasks that have already been
    completed. Uses the print_task() subroutine for formatting.'''

    completed_tasks = 0
    print("-"*80)
    with open(MY_PATH+"tasks.txt", "r", encoding="utf-8") as file:
        for line in file:
            contents = line.split(", ")
            if contents[5].strip() == "Yes":
                completed_tasks += 1
                print_task(line)
    print(f"There are {completed_tasks} completed tasks.")


def delete_task():
    '''Only for admin use. Enables the admin to delete a specified task
    using the task's title. Confirms before deletion.'''

    # Two lists to store all task information and just task titles.
    all_tasks = []

    with open(MY_PATH+"tasks.txt", "r", encoding="utf-8") as file:
        for line in file:
            all_tasks.append(line.strip())

    # Provide the user with numbers for all task names.
    print("Here are all of the present task names:")
    for i, task in enumerate(all_tasks):
        title = task.split(", ")[1].strip()
        print(f"{i+1}: {title}")

    # Check to make sure the user enters a valid entry.
    try:
        target_task = int(input("Please select a task number for deletion: "))
    except ValueError:
        print("Selection must be a number. Returning to main menu.")
        return

    if (target_task < 1) or (target_task > len(all_tasks)+1):
        print("An invalid number was given. Returning to main menu.\n")
        return

    # Valid number given; confirm it is the desired task for deletion.
    print(f"You have selected task {target_task}:")
    print_task(all_tasks[target_task-1])

    confirm = input("Are you sure you wish to delete this task (y/n)? : "
                    ).strip().lower()

    if confirm == "y":
        # Remove the target task and save the modified task list to
        # tasks.txt. WILL OVERWRITE tasks.txt.
        all_tasks.pop(target_task-1)
        with open(MY_PATH+"tasks.txt", "w", encoding="utf-8") as new_file:
            for j, t in enumerate(all_tasks):
                if j == len(all_tasks)-1:
                    new_file.write(t)
                else:
                    new_file.write(t+"\n")

    else:
        # No deletion; keep the tasks.txt the same as before.
        print("No task deletion. Returning to main menu.\n")
        return


# ==== Login Section ===================================================
# Check to make sure user.txt exist in the right place, open it, and
# store its contents in a dictionary.

valid_login_data = {}
try:
    with open(MY_PATH+"user.txt", 'r', encoding="utf-8") as my_file:
        for my_line in my_file:
            list_user, list_pw = my_line.split(",")
            list_user = list_user.strip()
            list_pw = list_pw.strip()
            valid_login_data.update({list_user: list_pw})
except FileNotFoundError:
    print("user.txt does not exist; please check the path and try again.")

# Check user's name and password for authentication.
# First check if the username is valid.
while True:
    current_user = input("Enter user name: ").strip()
    if current_user in valid_login_data:
        # Valid username entered; check for corresponding password.
        current_pw = input("Enter password: ").strip()
        if current_pw == valid_login_data[current_user]:
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
    if current_user == "admin":
        # Show all options for the admin.
        menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        vc - view completed tasks
        del - delete a particular task
        e - exit
    Selection: '''
                     ).strip().lower()

    else:
        # Show only certain options for non-admin.
        menu = input('''Select one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
    Selection: '''
                     ).strip().lower()

    if menu == 'r':
        # Register a new user and their password to user.txt.
        # ONLY ADMINS MAY DO THIS.
        if current_user == "admin":
            print("Registering a new user.\n")
            reg_user()
        else:
            print("Only admins may perform this action.\n")
            continue

    elif menu == 'a':
        # Add a new task and its requirements to the tasks.txt file.
        print("Adding a new task.")
        add_task()

    elif menu == 'va':
        # Format and display ALL current tasks.txt from file contents.
        print("Displaying all current tasks:")
        view_all()

    elif menu == 'vm':
        # Format and display current user's tasks from tasks.txt.
        print(f"Diplsaying all tasks for user: {current_user}.")
        view_mine(current_user)

    elif menu == 'vc':
        # Allow user to view completed tasks.
        # ONLY ADMINS MAY DO THIS.
        if current_user == "admin":
            print("Viewing completed tasks.\n")
            view_completed()
        else:
            print("Only admins may perform this action.\n")
            continue
    
    elif menu == 'del':
        # Allow user to delete a specified task.
        # ONLY ADMINS MAY DO THIS.
        if current_user == "admin":
            print("Deleting a task.\n")
            delete_task()
        else:
            print("Only admins may perform this action.\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
