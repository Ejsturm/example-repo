'''Create a minesweeper program. Input from user is 2D list of mines.
My job is to return the map with the digits filled in.
2025-05-27 EJS'''


def determine_adjacencies(row, col):
    """
    Determine the allowed rows and columns for a given entry. Prevents
    going out-of-bounds on the lists.
    """
    if row == 0:
        rows_to_check = [0, 1]
    elif row == field_rows-1:
        rows_to_check = [row-1, row]
    else:
        rows_to_check = [row-1, row, row+1]

    if col == 0:
        cols_to_check = [0, 1]
    elif col == field_cols-1:
        cols_to_check = [col-1, col]
    else:
        cols_to_check = [col-1, col, col+1]

    return (rows_to_check, cols_to_check)


def find_mines(row, col):
    """Tally up how many mines are adjacent (horizontally, vertically,
    or diagonally) to a given entry in the mine field."""

    # First identify the allowed rows and columns for a given entry
    row_options, col_options = determine_adjacencies(row, col)
    counter = 0
    for i in row_options:
        for j in col_options:
            if field[i][j] == "#":  # If a given entry is a mine.
                counter += 1
    return counter


# Welcome the user to the game
print("Welcome to Inverse Minesweeper. Input each row of the minefield.")
print("Use a # to indicate the location of a mine and - to indicate empty.")

field_rows = int(input("How many rows are in the field: "))
field_cols = int(input("How many columns are in the field: "))

# Obtain the minefield distribution from the user.
field = []
for r in range(0, field_rows):
    inp_row = input(f"Enter row {r+1}'s info,"
                    " use a space to separate entries: ").strip()
    field.append(inp_row.split(" "))

print("The initial field: ")
print(field)

# For each entry in the minefield, count the number of adjacent mines.
for r in range(field_rows):
    for c in range(field_cols):
        if field[r][c] == "#":
            # Skip mine entries, leave as is.
            continue
        field[r][c] = find_mines(r, c)

print("The 'solved' field: ")
print(field)
