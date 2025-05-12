# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Syntax error; added parentheses to 'print' call.
print("\n") # Syntax errors; inappropriate indentation removed and missing parenthesis added.

# Variables declaring the user's age, casting the str to an int, and printing the result
''' Several errors fixed below:
 Syntax: removed all unnecessary indentations from the 3 lines below.
 Syntax: removed extra = sign in variable declration for age_Str
 Runtime: fixed the age variable to only take the relevant part of the age_Str
 Runtime: added typecasting to the 'age' variable in the print statement.
 Logic: added spaces after "I'm" and before "years" to format it better.
'''
age_Str = "24 years old" 
age = int(age_Str[:2]) 
print("I'm " + str(age) + " years old.")

''' Several errors fixed below:
Syntax: removed all unnecessary indentations from the 3 lines below
Syntax: removed the quotation marks from the value assigned to years_from_now
Syntax: added parenthesis for the print function call
Logic: added space after "years:" for formatting
Logic: fixed the variable name in the print statement to be total_years instead of answer_years
Runtime: add typecasting to answer years and remove the quotation marks so that concatentation works.
'''
# Variables declaring additional years and printing the total years of age
years_from_now = 3
total_years = age + years_from_now
print("The total number of years: " + str(total_years))

''' Several errors fixed below:
Syntax: fixed variable name to be total_years instead of total.
Syntax: added parenthsis to print function call
Runtime: added typecasting to total_months in the print line.
Logic: added a period at the end of the sentence for sexiness.
'''
# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old.")

#HINT, 330 months is the correct answer

