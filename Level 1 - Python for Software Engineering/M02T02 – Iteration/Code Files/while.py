""" First while-loop experimentation. 2025-05-08 EJS"""

sum = 0
counter = 0

entry = int(input("Please enter a positive integer: "))
while entry:
    sum += entry
    counter += 1
    entry = int(input("Enter another positive integer. Use '-1' to end. "))
    if (entry == -1):
        break

print(f"The average is {sum/counter:.3f}.")