'''Copied the given debugging.py file and updating it. The goal is to
get the commented lines as output to STDOUT 2025-05-21 EJS'''


# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # Change argument to 'key'


# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh!",  # Used "" for string.
                         "maggie": "(Pacifier Suck)"
                         }


# In the line below, made the 3 strings elements of a single list.
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''