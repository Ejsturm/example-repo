""" The first capstone project. This program will enable the user to pick
a type of financial calculation, input relevant data, compute the desired
transation, and provide meaningful output. 
2025-05-08 EJS
"""

import math

print('''The available financial calculations are defined below.
      Investment - computes the interest you'll earn on an investment.
      Bond       - computes the amount you'll pay on a home loan.
      ''')


calculation_option = input("Please enter either 'investment' or 'bond' from "\
                           + "the menu above to proceed: ").lower()

# Normally I would encode a while loop or try-except or exit code to handle
# bad user entries so that the user could try again. However, we have not 
# coveredthose yet, so the *entire* script must be in the if-else structure 
# such that the entire program can execute and "finish."
# It is not clear to me if I'm allowed to use "future knowledge" at this 
# point or if that is bad form. Given that this is a portfolio entry, 
# what is the correct protocol? "Correct code" or "Only use what you have 
# been taught so far?" Please advise! (And I will remove this HUGE text 
# block, this is unsightly and DEFINITELY NOT PEP8 appropriate!) -EJS

if (calculation_option == "investment"):
    if (calculation_option == "investment"):
        # Ask the user for relevant investment details.
        # I assume that only valid entries are given!
        principal = float(input("Enter the initial deposit: "))

        # Convert the interest rate to a decimal value.
        rate = float(input("Enter the interest rate as a percent: "))
        rate = rate/100.0

        years = int(input("How many years will the investment take? "))
        interest_type = input("Will the interest be 'simple' or 'compound'? ").lower()

        if (interest_type == "simple"):
            total_money = principal * (1 + rate*years)
        else: # compound interest
            total_money = principal * math.pow((1+rate), years)
        # Round to appropriate value for money.
        total_money = round(total_money, 2)

        # The the user what they will earn.
        print("You will recieve ${:.2f} in total.".format(total_money))

elif(calculation_option == "bond"):
    # Ask the user for relevant bond loan information.
    initial_value = float(input("Enter the house's present value: "))

    # Convert the interest rate to a MONTHLY decimal value.
    rate = float(input("Enter the interest rate as a percent: "))
    rate = (rate/100)/12

    months = int(input("How many months will repayment take? "))

    # Compute monthly payment value.
    monthly_payment = (rate * initial_value) / \
        (1 - (1+initial_value)**(-1*months))
    # Round to appropriate value for money.
    monthly_payment = round(monthly_payment, 2)

    # Tell the user what they owe.
    print("Each month you will owe ${:.2f}.".format(monthly_payment))

else: # No valid option given.
    print("Invalid calculation type given. Exiting now.")