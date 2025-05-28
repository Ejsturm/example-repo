'''Create a program that takes a list and an index and sums all entries
up to and including the index's value. Use recursion. 2025-05-28 EJS'''


def adding_up_to(my_list, index):
    if index == -1:
        return 0
    else:
        return int(my_list[index]) + int(adding_up_to(my_list, index-1))


the_list = input("Enter a comma-seprated list of ints: ").strip().split(",")
the_end = int(input("Enter the final index to be summed: "))

total = adding_up_to(the_list, the_end)
print(f"The total is {total}.")
