'''Modify the given 'merge-sort' algorithm and modify it to sort
a list of strings based on their lengths. 2025-06-06 EJS'''


# Everything below is from the PDF's merge-sort.-------------------------------
def merge_sort(items):
    '''The original merge_sort thing.'''
    items_length = len(items)

    # # Create temporary storage for merging
    temporary_storage = [None] * items_length

    # Initialise the size of subsections to 1
    size_of_subsections = 1

    # Iterate until the size of subsections is less than the
    # length of the list
    while size_of_subsections < items_length:
        # Iterate over the list in steps of size_of_subsections*2
        for i in range(0, items_length, size_of_subsections*2):
            # Determine start & end indices of the 2 subsections to merge
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, items_length
            )
            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, items_length
            )

            # Define the sections to merge
            sections = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end
            )

            # Call the merge function to merge the subsections
            merge(items, sections, temporary_storage)

        # Double the size of subsections for the next iterations
        size_of_subsections *= 2

    # Return the sorted list
    return items


def merge(items, sections, tempoary_storage):
    '''The original merge thing.'''
    # Unpack the sections tuple to get the start & end indices of
    # each section
    (first_section_start, first_section_end), (
        second_section_start,
        second_section_end
    ) = sections

    # Initialise indices for the two sections and temp storage
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    # Loop until both sections have been fully merged
    while left_index < first_section_end or right_index < second_section_end:
        # Check if both sections still have elments to compare
        if left_index < first_section_end and right_index < second_section_end:
            # Compare elements from both sections
            # EJS: The line below has the changes that matter!
            if len(items[left_index]) < len(items[right_index]):
                # Place the smaller element into temp storage
                tempoary_storage[temp_index] = items[left_index]
                left_index += 1
            else:  # items[right_index] <= items[left_index]
                tempoary_storage[temp_index] = items[right_index]
                right_index += 1
            temp_index += 1

        # If section 1 still has elements left to merge
        elif left_index < first_section_end:
            # Copy remaining elements from section 1 to temporary storage
            for i in range(left_index, first_section_end):
                tempoary_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1

        # If section 2 still has elements left to merge
        else:  # right_index < second_section_end
            # Copy remaining elements from section 2 to temprary storage
            for i in range(right_index, second_section_end):
                tempoary_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1

    # Copy sorted elemnts from temp storage back to orginal list
    for i in range(temp_index):
        items[first_section_start+i] = tempoary_storage[i]


# EJS stuff starts--just a little test stuff first...
# print("\nBeginning now.")
# num_list = [5, 3, 2, 6, 1, 4, 8, 0, 9, 3, 6]
# sorted_num_list = merge_sort(num_list)
# print(f"\nThe sorted number list: {sorted_num_list}")

my_strings_1 = ['in', 'dog', 'I', 'food', 'socks',
                'messy', 'coffee', 'potato chips', 'airplane', 'robins']

my_strings_2 = ['alpha', 'beta', 'inspector', 'farce', 'cup',
                'tea', 'cat', 'hiccup', 'd20', 'fortified']

my_strings_3 = ['penguin', 'snag', 'lactose', 'Hokkaido', 'yarn',
                'memejac', 'mega stuff oreo', 'if', 'Chicago', 'chemistry']

print("\nSorting string list 1:")
sorted_list_1 = merge_sort(my_strings_1)
print(f"First list sorted: {sorted_list_1}.")

print("\nSorting string list 2:")
sorted_list_2 = merge_sort(my_strings_2)
print(f"Second list sorted: {sorted_list_2}.")

print("\nSorting string list 3:")
sorted_list_3 = merge_sort(my_strings_3)
print(f"Third list sorted: {sorted_list_3}.")
