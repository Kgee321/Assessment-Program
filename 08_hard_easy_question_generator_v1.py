"""Combinding 05_hard_easy_v1 with 07_question_generator_function_v2
so that if hard mode is entered, hard mode is played
and if easy mode is entered, easy mode is played
Written by Katelyn Gee
Created on the 15/05/2022
"""

import random


# Checker functions
def checker(question_text, question1, question2):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'program continues'
        if answer == question1 or answer == question1[0]:
            answer = question1.title()
            return answer

        # if they say no, out 'instructions displayed'
        elif answer == question2 or answer == question2[0]:
            answer = question2.title()
            return answer

        # otherwise - show error
        else:
            print(f"Please answer with '{question1}' or '{question2}'")


# Random question generator functions
def random_generator(lists, asking, num1, num2, num3, rounds):
    # Variables
    score = 0

    # Plays 5 rounds
    for i in range(rounds):

        # Mixes up the list so different question is chosen
        random.shuffle(lists)

        # Asks the user the question
        question = input(asking.format(lists[0][num2])).title()

        # if user got it right
        if question == lists[0][num1] or question == lists[0][num3]:
            answer = "right! Congratulations!"
            score += 1

        # if user got it wrong
        else:
            answer = f"wrong, the correct answer was '{lists[0][num1]}'. Try again next time! "

        # printing if user was right or wrong
        print(f"You got it {answer}")
        print()

        # To avoid questions being repeated, each question is removed once displayed
        lists.pop(0)
    return score


# asking user if they want easy mode or hard mode
hard_easy = checker("Do you want to play hard mode (h) or easy mode (e)? ", "hard", "easy")

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
number_of_rounds = 10

if hard_easy == "Easy":
    # User plays easy mode
    print("Easy Mode:\n")
    final_score = random_generator(numbers, "What is {} in English? ",
                                   0, 2, 1, number_of_rounds)
else:
    # User plays hard mode
    print("Hard Mode:\n")
    final_score = random_generator(numbers, "What is {} in Maori? ",
                                   2, 0, 0, number_of_rounds)
# printing final score
print(f"\nYou got {final_score} out of {number_of_rounds}")


