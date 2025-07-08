'''Update: modifying code to accomplish tasks 2 and 3. 2025-07-02 EJS

A capstone project at the end of 'Level 1.' Using the template given
as a foundation, modify it to enable users to login with a password,
choose a desired option from a menu, and execute tasks. There are
several subsequent tasks to upgrade the baseline program.

I will use version control along the way. 2025-06-12 EJS'''

# ===== Importing external modules ===========
from datetime import datetime as dt
from datetime import date

# Setting up path string to make future code more readable:
MY_PATH = ("c:/Users/sturm/Documents/ES25040017967/Level 1 - Python for "
           "Software Engineering/M03T10-Capstone_Project-Task_Manager/"
           "Code_Files/")

# Used for reading in and printing out dates in the desired format.
# EJS: I relied upon strftime.org for these format options.
DATE_STR_FORMAT = "%d %b %Y"

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
    current_date = str(date.today().strftime(DATE_STR_FORMAT))

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

    # Task updates can only be executed by 'view_mine()' and thus,
    # the admin would not see the other tasks not assigned to them.
    # However, as an admin, it is my decision to give them the
    # ability to update any task for any user so let them see those too.
    if user == "admin":
        print("********** Non-admin tasks **********")
        for i, task in enumerate(all_tasks):
            if task.split(", ")[0].strip() != "admin":
                print(f"{'Task number:': <20}{i+1}")
                print_task(task)
        print(f"\nThere are {user_tasks} admin tasks and {i} total tasks.\n")

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
        # If the task number is an illegal index, return to main menu.
        if (task_no < 1) or (task_no > len(all_tasks)):
            print("An invalid number was given. Returning to main menu.\n")
            return

        # If the user tries to modify a task that isn't assigned to
        # them, forbid the modification and return to main menu.
        # ADMINS MAY ALWAYS MODIFY ALL TASKS!!!

        # EJS: A professional software engineer tested my code and
        # suggested this functionality. I agreed it was smart and I
        # implemented it without further input.
        task_user = all_tasks[task_no-1]
        task_user = task_user.split(", ")[0].strip()
        if (user != "admin") and (task_user != user):
            print("You may not modify a task not assigned to you.")
            print("Returning to main menu.\n")
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
            print(f"Task {temp_task[1]} is now marked complete.")
            print("Returning to main menu.\n")
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


def generate_task_report():
    '''Creates a dictionary of stats about the tasks using the tasks.txt
    file. Everything needed for the task_overview.txt file is obtained
    or computed in this routine.

    Returns
    A dictionary with various data about task completion.'''

    task_data = {}  # Will hold all task statistics computed below.
    all_tasks = []  # Holds all tasks.txt data.

    total_tasks = 0
    with open(MY_PATH+"user.txt", 'r', encoding="utf-8") as task_file:
        for line in task_file:
            all_tasks.append(line.strip())
            total_tasks += 1

    # If the tasks.txt file is empty, notify the user.
    if total_tasks == 0:
        print('''No tasks exist; unable to generate statistics.
              Please add tasks before generating metadata.
              Returning to main menu.\n''')
        return task_data

    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0
    for t in all_tasks:
        task_components = t.split(", ")
        completion = task_components[5].strip()
        if completion == "Yes":
            completed_tasks += 1
        else:
            incomplete_tasks += 1
            # Determine the Unix time of the due date.
            # EJS: A pro software engineer taught me about the universal
            # unix timestamp concept.
            due_date_parse = dt.strptime(task_components[4], DATE_STR_FORMAT)

            # Compare the Unix timestamps to see if the task is overdue.
            if due_date_parse < dt.now():
                overdue_tasks += 1

    percent_incomplete = round(incomplete_tasks/total_tasks * 100, 2)
    percent_overdue = round(overdue_tasks/total_tasks * 100, 2)

    task_data.update({'Total tasks': total_tasks,
                      'Completed tasks': completed_tasks,
                      'Incomplete tasks': incomplete_tasks,
                      'Overdue tasks': overdue_tasks,
                      'Percent incomplete': percent_incomplete,
                      'Percent overdue': percent_overdue
                      })

    return task_data


def generate_user_dict():
    '''Collates task data according to the assigned user. Requires the
    user.txt and tasks.txt files. This is a support method for
    generate_report().

    Returns:
    total_users (int): the number of users in user.txt
    total_tasks (int): the number of tasks in tasks.txt
    all_user_data (dict): a nested dictionary where each key is a user
        and the value is another dictionary with raw task data.
    '''

    # All user data. A dictionary of dictionaries. Return this.
    all_user_data = {}

    total_users = 0
    # Get all users and initialize nested dictionary structure.
    with open(MY_PATH+"user.txt", 'r', encoding="utf-8") as user_file:
        for line in user_file:
            total_users += 1
            user = line.split(", ")[0].strip()
            all_user_data.update({user: {
                "total tasks": 0,
                "complete": 0,
                "incomplete": 0,
                "overdue": 0}})

    total_tasks = 0
    # Extract task data to get raw numerical data on assigned tasks.
    # Update nested dictionary values.
    with open(MY_PATH+"tasks.txt", 'r', encoding="utf-8") as task_file:
        for task in task_file:
            total_tasks += 1
            contents = task.split(", ")
            assignee = contents[0]
            completion = contents[5].strip()
            due_date = dt.strptime(contents[4].strip(), DATE_STR_FORMAT)

            # Update the user's total number of tasks.
            all_user_data[assignee]["total tasks"] += 1

            # Update the user's complete/incomplete task number.
            if completion == "Yes":
                all_user_data[assignee]["complete"] += 1
            else:
                all_user_data[assignee]["incomplete"] += 1
                # Determine whether an incomplete task is overdue and
                # update accordingly.
                if due_date < dt.now():
                    all_user_data[assignee]["overdue"] += 1

    return total_users, total_tasks, all_user_data


def generate_reports():
    '''This subroutine calls two subroutines since I think each report
    should be its own function. The additional support subroutines have
    appropriate detail for the report type generated, user vs. task.'''

    # Create two dictionaries to store relevant info.
    # Populate them in support subroutines.
    task_stats = generate_task_report()
    if not task_stats:
        # If there were no tasks, go back to the main menu.
        # Error message sent to STDOUT in generate_task_report().
        return

    total_users, total_tasks, raw_user_stats = generate_user_dict()

    # Compute requisite statistics using raw user data.


def display_statistics():
    '''Opens the overview text files (created by generate_reports()) and
    display the contents in a formatted output for the user. If the text
    files do not exist, call generate_reports() first.'''
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
        # ONLY ADMINS MAY DO THIS.
        # Register a new user and their password to user.txt.
        if current_user == "admin":
            print("Registering a new user.\n")
            reg_user()

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
        # ONLY ADMINS MAY DO THIS.
        # Allow user to view completed tasks.
        if current_user == "admin":
            print("Viewing completed tasks.\n")
            view_completed()

    elif menu == 'del':
        # ONLY ADMINS MAY DO THIS.
        # Allow user to delete a specified task.
        if current_user == "admin":
            print("Deleting a task.\n")
            delete_task()

    elif menu == 'ds':
        # ONLY ADMINS MAY DO THIS.
        # Diplay the information stored in the report files.
        display_statistics()

    elif menu == 'gr':
        # ONLY ADMINS MAY DO THIS.
        # Allow user to generate two report text files.
        if current_user == "admin":
            generate_reports()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
