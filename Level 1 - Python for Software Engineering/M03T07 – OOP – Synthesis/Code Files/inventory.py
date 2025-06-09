'''This project enables a user to search through a warehouse's inventory
and learn about a given shoe's details. Output must be formatted in a
nice, easy-to-read manner. 2025-06-08 EJS


========The beginning of the class==========
'''


class Shoe:
    '''This class holds info for each shoe in a warehouse.'''
    def __init__(self, country, code, product, cost, quantity):
        '''The initializer for a shoe object.'''
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''Returns how much a particular shoe costs.'''
        return self.cost

    def get_quantity(self):
        '''Returns how many shoes of this type are in stock.'''
        return self.quantity

    def set_quantity(self, stock):
        '''Reset the quantity value.

        EJS: I thought this was a necessary subroutine to add since the
        'restock' subroutine requires this functionality and I did not
        think that having an external subroutine do this was appropriate
        from a scope perspective.'''
        self.quantity = stock

    def __str__(self):
        '''Returns formatted information about a shoe.'''
        return f"""Shoe details:
        Product name:................{self.product}
        ID code:.....................{self.code}
        Origin country:..............{self.country}
        Cost:........................{self.cost}
        Stock quantity:..............{self.quantity}"""


# =============Shoe list===========
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data(my_list):
    '''
    Read in the inventory.txt file, create a new shoe object for each
    line, append the shoe to the passed list.

    Args:
    my_list (list): A list of shoe inventory to be added to.

    Returns:
    The populated list.
    '''
    file_name = input("Provide the file name (with path if needed): ").strip()
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # EJS: I used stackexchange to learn how to skip first line.
            lines = file.readlines()[1:]
            for line in lines:
                country, code, product, cost, quantity = line.split(",")
                new_shoe = Shoe(country, code, product, cost, quantity)
                my_list.append(new_shoe)

    except FileNotFoundError:
        print("The file does not exist; check file name and path.")

    return my_list


def capture_shoes(my_list):
    '''Enables the user to manually enter a new shoe into inventory by
    asking the user for relevant information.

    Args:
    my_list (list): A list of shoe inventory to be added to.

    Returns:
    The list with a single new shoe added to it.
    '''
    # Ask user for new info
    new_product = input("Product name: ")
    new_id = input("ID value: ")
    new_country = input("Origin country: ")

    # Ensure these two fields are given as integers
    try:
        new_cost = int(input("Cost: "))
    except ValueError:
        print("The cost must be an integer. Returning to main menu.\n")
        return my_list
    try:
        new_inventory = int(input("How many in stock: "))
    except ValueError:
        print("The number of items in stock must be an integer. "
              "Returning to main menu.\n")
        return my_list

    # Check with the user to confirm accuracy before adding the item
    print("Is the following information correct?\n"
          f"\tProduct name:................{new_product}\n"
          f"\tID code:.....................{new_id}\n"
          f"\tOrigin country:..............{new_country}\n"
          f"\tCost:........................{new_cost}\n"
          f"\tStock quantity:..............{new_inventory}"
          )
    accurate = input("Is the above information accurate? (y/n): ")
    accurate.strip().lower()

    if accurate == "y":
        # If the user is satisfied, add a new shoe item to the list.
        new_shoe = Shoe(new_country, new_id, new_product, new_cost,
                        new_inventory)
        my_list.append(new_shoe)
    else:
        # Something went wrong with data entry, do not add new shoe.
        print("Manual entry failed, returning to main menu.\n")

    return my_list


def view_all(my_list):
    '''Print all data for each item in inventory.
    EJS: I did not want to muck around with pip to get the tabulate
    library installed at this time.

    Args:
    my_list (list): the full inventory

    Returns:
    None
    '''
    for shoe in my_list:
        print(shoe)
    print("End of inventory.\n")


def re_stock(my_list):
    '''Search through the entire inventory to find the shoe that has the
    fewest items in stock and ask the user if they'd like to restock it.

    Note: in the event that more than one shoe has a minimum, only the
    first will have the option to update; this subroutine would have to
    be run more than once to update all 'tied' inventory entries!

    Note 2: while one could reset the inventory here, I decided to write
    a new subroutine within the Shoe class to reset the quantity value.

    Args:
    my_list (list): the full inventory

    Returns:
    The inventory list which may/may not have been updated.
    '''
    min_stock = 1e12  # Initialized this to an imporobably large value
    min_index = len(my_list) + 1  # Initialized to an illegal index

    # Find the item with the lowest inventory
    for index, shoe in enumerate(my_list):
        stock = shoe.get_quantity()
        if stock < min_stock:
            min_stock = stock
            min_index = index

    # Show the user the shoe with the lowest stock.
    print("The item with the lowest stock is displayed below:")
    print(my_list[min_index])

    # Would they like to restock this item?
    update = input("Would you like to restock this shoe? (y/n) ")
    update = update.strip().lower()

    # Update stock if specified and show the updated entry.
    if update == "y":
        new_quantity = int(input("Enter new inventory number: ").strip())
        my_list[min_index].set_quantity(new_quantity)
        print("The item has been updated:")
        print(my_list[min_index])

    return my_list


def search_shoe(my_list):
    '''Search the inventory for a specified target and display the
    entry if it exists.

    Args:
    my_list (list): the full inventory

    Returns:
    None
    '''
    target = input("Provide the ID code: ").strip().upper()
    found = False
    for shoe in my_list:
        if shoe.code == target:
            found = True
            print(shoe)

    if found is False:
        print("The specified ID did not match any shoe in the inventory. "
              "Please check the ID code and try again.\n")


def value_per_item(my_list):
    '''Print the total value for each item in the inventory using the
    formula value = cost*quantity.

    Args:
    my_list (list): the full inventory

    Returns:
    None
    '''
    for shoe in my_list:
        cost = shoe.get_cost()
        quantity = shoe.get_quantity()
        value = cost * quantity
        name = shoe.product

        # EJS: I used stackoverflow.com to learn the format syntax here.
        print(f"Value of {name:<24}:{value:>8}.")
    print()


def highest_qty(my_list):
    '''Find the item with the highest stock quantity and print that
    it is on sale.

    Note: only the first maximal value is printed. If there is a tie,
    that will NOT be captured here. Running the routine again will not
    find it either, only a change in stock quantity will change the
    result of this subroutine.

    Args:
    my_list (list): the complete inventory

    Returns:
    None
    '''
    max_quantity = 0  # Initialize to a minimal value.
    max_index = len(my_list) + 1  # Initialize to an illegal index.

    for index, shoe in enumerate(my_list):
        quantity = shoe.get_quantity()

        # Strictly greater than such that only the 'first' max value is
        # reported; if there is another item later on, that will not be
        # put on sale.
        if quantity > max_quantity:
            max_quantity = quantity
            max_index = index

    # A maximum has been found. Report it as being on sale.
    product = my_list[max_index].product
    print(f"The '{product}' shoe has the most items with {max_quantity} in "
          "stock. This item should be put on sale!\n")


# ==========Main Menu=============
print("Welcome to the Shoe Inventory Program.")
selection = -1
while selection != 0:
    print("Please select an option from the following menu:")
    print("""\t1: Read in shoe data from an external file
        2: Add a new shoe to the inventory
        3: View all inventory
        4: Find and re-stock lowest inventory item
        5: Find a specific shoe based on code
        6: Print all shoe values
        7: Create a sale for the shoe with the most inventory in stock
        0: Exit program
        """)

    # Use try-except to ensure the selection is an integer.
    try:
        selection = int(input("\tSelection choice: "))

        # Execute user's selected option; if selection is an invalid entry,
        # prompt them to try again (repeat while-loop again).
        if selection == 1:
            print("Reading in an external data file.")
            shoe_list = read_shoes_data(shoe_list)
        elif selection == 2:
            print("Manual entry of a new shoe to the inventory.")
            shoe_list = capture_shoes(shoe_list)
        elif selection == 3:
            print("Displaying all inventory.")
            view_all(shoe_list)
        elif selection == 4:
            print("Restocking the lowest stock item.")
            shoe_list = re_stock(shoe_list)
        elif selection == 5:
            print("Seeking a particular shoe's info based upon ID.")
            search_shoe(shoe_list)
        elif selection == 6:
            print("Displaying all total shoe values.")
            value_per_item(shoe_list)
        elif selection == 7:
            print("Creating a sale for the shoe with the most stock.")
            highest_qty(shoe_list)
        elif selection == 0:
            # Exit program
            print("Thank you for using the Shoe Inventory Program. "
                  "Exiting now.\n")
            break
        else:
            # An integer that is not [0,7] was given and is not invalid.
            print("Invalid option given; selection must be a number between "
                  "0-7.\n")
    except ValueError:
        print("Selection must be a number, please try again.\n")
