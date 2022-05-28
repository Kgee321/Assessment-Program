"""Component 4 (Random Generator) -- Version 3 -- Trial 2
Trying a different way of choosing a random question
by having answers and questions in one long list
and shuffling the list.
Written by Katelyn Gee
Created 9/05/2022"""

import random

# List of English and Maori numbers
numbers = [["1", "Tahi"],
           ["2", "Rua"],
           ["3", "Toru"],
           ["4", "Wha"],
           ["5", "Rima"],
           ["6", "Ono"],
           ["7", "Whitu"],
           ["8", "Waru"],
           ["9", "Iwa"],
           ["10", "Tekau"]]

# Plays 5 rounds
for i in range(5):

    # Mixes up the list so different question is chosen
    random.shuffle(numbers)

    # Asks the user the question
    question = input("What is {} in English? ".format(numbers[0][1])).title()

    # If user got it right
    if question == numbers[0][0]:
        answer = "right!"

    # If user got it wrong
    else:
        answer = "wrong"

    # Printing if user is right or wrong
    print(f"You got it {answer}")
    print()
