"""Component 4 (Random Generator) -- Version 3 -- Trial 2
Trying a different way of choosing a random question
by having answers and questions in one long list
and shuffling the list.
Written by Katelyn Gee
Created 9/05/2022"""

import random

# List of English and Maori numbers
numbers = [["1", "One", "Tahi"],
           ["2", "Two", "Rua"],
           ["3", "Three", "Toru"],
           ["4", "Four", "Wha"],
           ["5", "Five", "Rima"],
           ["6", "Six", "Ono"],
           ["7", "Seven", "Whitu"],
           ["8", "Eight", "Waru"],
           ["9", "Nine", "Iwa"],
           ["10", "Ten", "Tekau"]]

# Plays 5 rounds
for i in range(5):

    # Mixes up the list so different question is chosen
    random.shuffle(numbers)

    # Asks the user the question
    question = input("What is {} in English? ".format(numbers[0][2])).title()

    # if user got it right -- numbers
    if question == numbers[0][0] or question == numbers[0][1]:
        answer = "right!"

    # if user got it wrong
    else:
        answer = "wrong"

    print(f"You got it {answer}")
    print()
