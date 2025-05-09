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

if (calculation_option == "investment"):
    if (calculation_option == "investment"):
        # Ask the user for relevant investment details.
        # I assume that only valid entries are given!
        principle = float(input("Enter the initial deposit: "))

        # Convert the interest rate to a decimal value.
        rate = float(input("Enter the interest rate as a percent: "))
        rate = rate/100.0

        years = int(input("How many years will the investment take? "))
        interest_type = input("Will the interest be 'simple' or 'compound'? ").lower()

        if (interest_type == "simple"):
            total_money = principle * (1 + rate*years)
        else: # compound interest
            total_money = principle * math.pow((1+rate), years)
        # Round to appropriate value for money.
        total_money = round(total_money, 2)

        # Tell the user what they will earn.
        print("You will recieve ${:.2f} in total.".format(total_money))

elif(calculation_option == "bond"):
    # Ask the user for relevant bond loan information.
    initial_value = float(input("Enter the house's present value: "))

    # Convert the interest rate to a MONTHLY decimal value.
    rate = float(input("Enter the interest rate as a percent: "))
    rate = (rate/100)/12

    months = int(input("How many months will repayment take? "))

    # Compute monthly payment value and round appropriately.
    monthly_payment = (rate * initial_value) / \
        (1 - (1+rate)**(-1*months))
    monthly_payment = round(monthly_payment, 2)

    # Tell the user what they owe.
    print("Each month you will owe ${:.2f}.".format(monthly_payment))

else: # No valid option given.
    print("Invalid calculation type given. Exiting now.")