"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730521912"

word_input = input("Enter a 5-character word: ")
if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_char = input("Enter a single character: ")
if len(single_char) !=1 or single_char == " ":
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_char + " in " + word_input)
count_instance = 0
if word_input[0] == single_char:
    print(single_char + " found" + " at index 0")
    count_instance += 1
if word_input[1] == single_char:
    print(single_char + " found" + " at index 1")
    count_instance += 1
if word_input[2] == single_char:
    print(single_char + " found" + " at index 2")
    count_instance += 1
if word_input[3] == single_char:
    print(single_char + " found" + " at index 3")
    count_instance += 1
if word_input[4] == single_char:
    print(single_char + " found" + " at index 4")
    count_instance += 1
if count_instance == 0:
    print("No instances of " + single_char + " found in " + word_input)
elif count_instance == 1:
    print(str(count_instance) + " instance of " + single_char + " found in " + word_input)
else:
    print(str(count_instance) +" instances of " + single_char + " found in " + word_input)