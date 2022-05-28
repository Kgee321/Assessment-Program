"""Base component -- Version 1
Welcome screen created here
Also asks for user's name
Adding each component as they are created
Not much editing done to the code
Written by Katelyn Gee
created on 3/05/2022
"""

import random


# number checker
def num_checker(question, low, high, answer1, answer2):

    # Stored Variable
    ERROR = "Please enter a whole number \n"

    # Keep asking until a valid number is entered
    while True:
        try:

            # Ask users age
            age = int(input(question))

            # Checking if age between the boundary's
            if age < low:
                return answer1
            elif age > high:
                return answer2
            else:
                return age

        except ValueError:
            print(ERROR)


# Checker functions
def checker(question_text, question1, question2):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If user answers first response
        if answer == question1 or answer == question1[0]:
            answer = question1.title()
            return answer

        # If user answers second response
        elif answer == question2 or answer == question2[0]:
            answer = question2.title()
            return answer

        # Otherwise - show error
        else:
            print(f"Please answer '{question1}' or '{question2}'")


# Instructions functions
def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")


# Random question generator functions
def random_generator(lists, asking, num1, num2, num3, rounds):
    # Variables
    score = 0

    # Rounds played
    for i in range(rounds):

        # Mixes up the list so different question is chosen
        random.shuffle(lists)

        # Asks the user the question
        question = input(asking.format(lists[0][num2])).title()

        # If user got it right
        if question == lists[0][num1] or question == lists[0][num3]:
            answer = "right! Congratulations!"
            score += 1

        # If user got it wrong
        else:
            answer = f"wrong, the correct answer was '{lists[0][num1]}'. Try again next time! "

        # Printing if user was right or wrong
        print(f"You got it {answer}")
        print()

        # To avoid questions being repeated, each question is removed once displayed
        lists.pop(0)

    return score


# Welcome screen
print(f"{'--'*10} Maori Numbers 1 to 10 Quiz {'--'*10}")
print()

# User name
name = input("What is your name? ").title()
print(f"Welcome {name}")
print()

# User age
user_age = num_checker(f"What is your age, {name}? ", 5, 12, "young", "old")

# Checking if user is too old or too young
if user_age == "young" or user_age == "old":
    print(f"Sorry {name}, you are too {user_age} to play")
    quit()

# Yes/No checker
played_before = checker("Have you played this quiz before (y/n)? ", "yes", "no")
print()

# Instructions displayed
if played_before == "No":
    instructions()

# Asking user if they want easy/hard mode
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

if hard_easy == "Easy":

    # User plays easy mode
    print("Easy Mode:\n")
    final_score = random_generator(numbers, "What is {} in English? ", 0, 2, 1, 10)
else:

    # User plays hard mode
    print("Hard Mode:\n")
    final_score = random_generator(numbers, "What is {} in Maori? ", 2, 0, 0, 10)

# Printing final score and farewell
print(f"\nYou got {final_score} out of 10")
print()
print("Nice Job! Farewell ")
