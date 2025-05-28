'''Create a recursive function to find the largest number in a list.
This is a contrived, silly question to ask. 2025-05-28 EJS'''


def find_largest(my_list):
    if len(my_list) == 1:
        return int(my_list[0])
    if int(my_list[0]) >= int(my_list[1]):
        my_list.pop(1)
    else:
        my_list.pop(0)
    find_largest(my_list)
    return int(my_list[0])


int_list = input("Enter ints with comma separators: ").strip().split(",")
largest = find_largest(int_list)
print(f"The largest value is {largest}.")
