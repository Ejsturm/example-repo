"""Use a for loop to make a pattern print to STDOUT. 2025-05-08 -EJS"""

subtrahend = 0 # The number to be subtracted.

for line in range(1, 9):
    if line >= 6:
        subtrahend += 2
    print("*"*(line-subtrahend))