"""Beginning with the given class template, replace the <pass>
statements with code to make a functional email simulator.
2025-05-21 EJS


Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.


# --- OOP Email Simulator --- #

# --- Email Class --- #
Create the class, constructor and methods to create a new Email object.
EJS: my code begins here with the definition of the class.
"""


class Email:
    """Create the email class.
    Initialise the instance variables for each email.
    Class variables"""
    has_been_read = False

    # Constructor, no defaults
    def __init__(self, address, subject, content):
        self.address = address
        self.subject = subject
        self.content = content

    def mark_as_read(self):
        """Create the 'mark_as_read()' method to change the 'has_been_read'
        instance variable for a specific object from False to True."""
        self.has_been_read = True


# --- Functions --- #
# Build out the required functions for your program.

# This list will hold all the email (objects).
inbox = []


def populate_inbox():
    """Create 3 sample emails and add them to the inbox list."""
    inbox.append(Email("monty@python.circus", "Norwegian Blue",
                       "This is an ex-parrot!"))
    inbox.append(Email("alastor@hazbin.hotel", "New Bartender",
                       "There is a new bartender named Husk."))
    inbox.append(Email("murderbot@sanctuary.moon", "Best episode?",
                       "Was episode 314 the best one yet?"))


def list_emails():
    """Create a function that prints each email's subject line
    alongside its corresponding index number,
    regardless of whether the email has been read."""
    for i, e in enumerate(inbox, start=1):
        print(f"Email #{i}'s subject is: {e.subject}")


def read_email(index):
    """Create a function that displays the email_address, subject_line,
    and email_content attributes for the selected email.
    After displaying these details, use the 'mark_as_read()' method
    to set its 'has_been_read' instance variable to True."""
    address = inbox[index].address
    subject = inbox[index].subject
    content = inbox[index].content

    inbox[index].mark_as_read()

    print(f"\nThe email at index {index} is titled '{subject}.'\nIt was sent "
          f"by {address}.\nThe contents are: {content}\nThis email is now "
          f"marked read.")


def view_unread_emails():
    """Create a function that displays all unread Email object subject lines
    along with their corresponding index numbers.
    The list of displayed emails should update as emails are read."""
    for i, _ in enumerate(inbox):
        if inbox[i].has_been_read is False:
            subject = inbox[i].subject
            print(f"{subject}")


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        email_index = -1
        while (email_index not in [0, 1, 2]):
            email_index = int(input("Enter email index to be read: "))
        read_email(email_index)

    elif user_choice == 2:
        # Add logic here to view unread emails
        print("The emails below are unread at the time of query.\n")
        view_unread_emails()

    elif user_choice == 3:
        # Add logic here to quit application.
        print("\n---Exiting application now.---\n")
        break

    else:
        print("Oops - incorrect input.")
