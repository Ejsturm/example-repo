'''A program that will take a user's input string and alternate upper versus lower cas
either every other letter, or every other word. 2025-05-12 EJS'''

# Ask for a sentence and prepare it by setting the case and removing whitespace
original_sentence = input("Please input a string: ")
print("The original sentence:\n" + original_sentence)
sentence = original_sentence.strip()

# First alternate the case of individual characters.
# Upper case first, then lower.
alternate_letters_list = []
for i in range(len(sentence)):
    if (i % 2) == 0: # even letters
        letter = sentence[i].upper()
    else: # odd letters
        letter = sentence[i].lower()
    alternate_letters_list.append(letter)
    alternate_letters_sentence = "".join(alternate_letters_list)
print("\nThe alternate-case letter version:\n" + alternate_letters_sentence)

# Now alternate case of separate words. 
# Lower first, then upper.
word_split = sentence.split()
alternate_word_list = []
for i in range(len(word_split)):
    if (i % 2) == 0: #even numbered words
        word = word_split[i].lower()
    else: #odd numbered words
        word = word_split[i].upper()
    alternate_word_list.append(word)
    alternate_word_sentence = " ".join(alternate_word_list)
print("\nThe alternate-case words version:\n" + alternate_word_sentence)