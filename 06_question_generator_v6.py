"""Component 4 (Random Generator) -- Version 6
Using  06_v3 as the base of this code.
Changing amount of questions asked to 10 (because there is 10 questions possible)
Also adding feedback to the user by telling them the correct answer when they get it wrong.
Removing te rao numbers so questions do not repeat in one game
Written by Katelyn Gee
Created 11/05/2022"""

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

# Variables
score = 0

# Plays 5 rounds
for i in range(10):

    # Mixes up the list so different question is chosen
    random.shuffle(numbers)

    # Asks the user the question
    question = input("What is {} in English? ".format(numbers[0][2])).title()

    # if user got it right
    if question == numbers[0][0] or question == numbers[0][1]:
        answer = "right! Congratulations!"
        score += 1

    # if user got it wrong
    else:
        answer = f"wrong, the correct answer was '{numbers[0][0]}' "

    # printing if user was right or wrong
    print(f"You got it {answer}")
    print()

    # Removing questions and their answer's to avoid questions repeating
    numbers.pop(0)

