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
        print("That user name already exists. Returning to main menu.\n")
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
    print(f"{'Task name:': <20}{contents[1]}")
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
    print_task() subroutine for formatting. The user may also select a
    task and edit the following options: completeness flag, assinged
    user, or due date. Updates are handled by update_task().

    Parameters:
    user (string): the current username
    '''

    user_tasks = 0  # Tasks assigned to current user.
    all_tasks = []  # A list to store all task information

    with open(MY_PATH+"tasks.txt", "r", encoding="utf-8") as file:
        for line in file:
            all_tasks.append(line.strip())

    # Print all user's tasks (Task 1's requirement.)
    print("-"*80)
    for i, task in enumerate(all_tasks):
        # Check task's assinged person and print its details if it
        # matches the current username.
        if task.split(", ")[0].strip() == user:
            user_tasks += 1
            print(f"{'Task number:': <20}{i+1}")
            print_task(task)
    print(f"The user {user} has {user_tasks} tasks assigned to them.\n")

    # If the task is not complete, offer the option to 'complete' or
    # edit it. (Task 3's requirement.)
    print("To update a task, enter the task number.")
    print("\tTo return to the main menu, enter -1")

    try:
        task_no = int(input("\tTask for modification: ").strip())

    except ValueError:
        print("Selection must be a number. Reutrning to main menu.\n")
        return

    if task_no == -1:
        print("Returning to main menu.\n")
    else:
        if (task_no < 1) or (task_no > len(all_tasks)):
            print("An invalid number was given. Returning to main menu.\n")
            return

        # Only incomplete tasks may be updated, so check it.
        task_status = all_tasks[task_no-1]
        task_status = task_status.split(", ")[5].strip()
        if task_status == "Yes":
            print("Task is already complete and cannot be modified.")
            print("Returning to main menu.\n")
        else:
            update_task(all_tasks, task_no-1)


def update_task(tasks, target):
    '''Provide the user with options to update a single task. If the
    task is marked 'complete' no further edits are permitted. If the
    task is incomplete, the user and/or due date may be updated. The
    tasks are saved to task.txt at the end no matter what.

    This subroutine is a support for the 'vm' main menu option, part of
    Task 3's requirements. -EJS

    Parameters:
    tasks (list of str): a list where each entry is a single task

    target (int): the 0-indexed task number for modification'''

    # Obtain the appropriate task for modification; modify a 'temporary'
    # copy and overwrite the original task entry at the end.
    temp_task = tasks[target]
    temp_task = temp_task.split(", ")

    # Begin edit menu.
    while True:
        option = input('''Select an update option:
        c - complete task
        u - update assigned user
        d - update the due date
        e - exit task edit mode
        Selection: ''').strip().lower()

        if option == 'c':
            temp_task[5] = "Yes"
            # Once a task is complete, no further edits are permitted.
            # Therefore, break out of the menu while loop.
            break
        elif option == 'u':
            new_name = input("Who should be assinged to this task: ").strip()
            temp_task[0] = new_name
        elif option == 'd':
            new_date = input("New due date (DD Mon YYYY): ").strip()
            temp_task[4] = new_date
        elif option == 'e':
            print("Exiting task editing menu.")
            break
        else:
            print("Invalid entry. Please try again.")

    # All desired edits are complete. Rejoin the list to make a single
    # string for overwriting the target entry in tasks.txt.
    temp_task = ", ".join(temp_task)
    tasks[target] = temp_task

    # Save updates to task.txt.
    with open(MY_PATH+"tasks.txt", "w", encoding="utf-8") as new_file:
        for j, t in enumerate(tasks):
            if j == len(tasks)-1:
                new_file.write(t)
            else:
                new_file.write(t+"\n")


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

    # A list to store all task information.
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
        print("Selection must be a number. Returning to main menu.\n")
        return

    if (target_task < 1) or (target_task > len(all_tasks)):
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


def generate_repots():
    pass


def display_statistics():
    pass


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
        ds - display statistics
        gr - generate reports
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

    elif menu == 'ds':
        # Allow user to
        # ONLY ADMINS MAY DO THIS.
        display_statistics()

    elif menu == 'gr':
        # Allow user to generate two report text files.
        # ONLY ADMINS MAY DO THIS.
        if current_user == "admin":
            generate_reports()
        else:
            print("Only admins may perform this action.\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
