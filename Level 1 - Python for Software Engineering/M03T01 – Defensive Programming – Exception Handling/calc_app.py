'''A calculator application designed to allow a user to select an
operation, input two numbers, and writes the equation to an output
file, all while handling errors. 2025-05-21 EJS'''

user_choice = input("Would you like to do a new calculation or print "
                    "previous calculations? [calculate, print]: "
                    ).strip().lower()
while (user_choice not in ["calculate", "print"]):
    user_choice = input("Invalid option, try again: ").strip().lower()

file = None
if (user_choice == "print"):
    try:
        file = open("equations.txt", "r")
        for line in file:
            print(line)
    except FileNotFoundError as error:
        print("The file you are trying to open does not exist.")
        print(error)
    finally:
        if file is not None:
            file.close()

else:  # Perform a calculation
    # Valid options
    operation_list = ["add", "subtract", "multiply", "divide"]

    # Get user's operation choice
    operation = input("Please choose an operation from the following "
                      "options: add, subtract, multiply, divide: "
                      ).strip().lower()
    while operation not in operation_list:
        operation = input("Invalid entry, please try again: ").strip().lower()

    # Get user's input numbers
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("That is not a number. Try again.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("That is not a number. Try again.")

    # Execute desired operation on input numbers
    result = None
    op_string = ""
    if (operation == "add"):
        op_string = "+"
        result = num1 + num2
    elif (operation == "subtract"):
        op_string = "-"
        result = num1 - num2
    elif (operation == "multiply"):
        op_string = "*"
        result = num1 * num2
    elif (operation == "divide"):
        try:
            op_string = "/"
            result = num1 / num2
        except ZeroDivisionError:
            result = "NaN"
            print("You are trying to divide by zero!")
    else:
        print("Something has gone terribly wrong if this prints.")

    # Construct the output equation as a string
    if (result == "NaN"):
        # This case handles division by 0.
        out_string = f"{num1} {op_string} {num2} = NaN\n"
    else:
        out_string = f"{num1} {op_string} {num2} = {result:.4f}\n"

    # Print full equation and result to output file.
    file = None
    try:
        file = open("equations.txt", "a")
        file.write(out_string)
        file.close()
    except FileNotFoundError as error:
        print("The file you are trying to open does not exist.")
        print(error)
    finally:
        if file is not None:
            file.close()
