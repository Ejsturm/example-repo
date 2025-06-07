'''Using a given list, write algorithsm to search and then insertion-
sort into it. I also implement a binary search algorithm after sorting
the data using built-in sorting methods. 2025-06-01 EJS'''

original_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Q1: Because the given list is not ordered, I believe that linear
#     is the best choice here. Without ordering, a more 'intelligent'
#     search  algorithm cannot function. Linear is the only choice.


def linear_search(my_list, target):
    '''Q2: The linear search algorithm implementation.'''
    for i, _ in enumerate(my_list):
        if target == my_list[i]:
            return f"The target {target} was found at index {i}."


def insertion_sort(unsorted):
    '''Q3: implementation of the insertion_sort algorithm.'''
    i_list = [unsorted[0]]  # Begin with the 1st entry of unsorted.
    for i in range(1, len(unsorted)):
        if unsorted[i] >= i_list[-1]:
            # If the next unsorted entry is greater than the max sorted
            i_list.append(unsorted[i])
        elif unsorted[i] <= i_list[0]:
            # If the next unsorted entry is less than the min sorted
            i_list = [unsorted[i]] + i_list
        else:
            # All other unsorted elements must be placed within sorted.
            # The 'if' statement identifies the two adjacent elements
            # where the new unsorted element will be inserted.
            for j, _ in enumerate(i_list):
                if unsorted[i] >= i_list[j] and unsorted[i] <= i_list[j+1]:
                    i_list = i_list[0:j+1] + [unsorted[i]] + i_list[j+1:]
                else:
                    # This is required to continue the for loop.
                    continue
                # Once the correct location is found, do not continue
                # with this for-loop, go back to the main for-loop.
                break
    return i_list


def binary_search(my_list, index, target):
    '''Q4: I've implemented a recursive binary search. In the real world
    this would be useful with an ordered (numerical) list, perhaps like
    a library's holdings. If the numbers are associated with a position,
    then the user could find the location quickly. '''
    midvalue = len(my_list)//2
    list_len = len(my_list)
    if list_len == 1 and target != my_list[midvalue]:
        return -1
    elif my_list[midvalue] < target:
        # The target is more than midvalue.
        index += list_len//2
        index = binary_search(my_list[midvalue:], index, target)
        return index
    elif my_list[midvalue] > target:
        # The target is less than midvalue.
        index = binary_search(my_list[:midvalue], index, target)
        return index
    elif my_list[midvalue] == target:
        # The target is at the middle value.
        index += 1
        return index
    return index


print(f"The original list: {original_list}")
# Running each of the subroutines in order.
# For Q1 and Q2: the linear search:
result = linear_search(original_list, 9)
print(f"\nThe linear search result:\n{result}")

# For Q3: the insertion search
sorted_list = insertion_sort(original_list)
print("\nThis is the insertion-sorted list:")
print(sorted_list)

# For Q4: binary search
sorted_copy = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
sorted_copy.sort()
print("\nAnd finally, the binary search on a sorted list:")
my_target = 5
target_index = binary_search(sorted_copy, 0, my_target)
print(f"The target {my_target} is at index {target_index}.")
