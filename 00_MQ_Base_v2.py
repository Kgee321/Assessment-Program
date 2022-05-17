"""Base component -- Version 1
Adding user's name in places to make the user feel appreciated
Put in formatter function to make important statements stand out
Add in the round number into random_generator function
Also adding in the instructions
Written by Katelyn Gee
created on 18/05/2022
"""

import random


# Number checker function
def num_checker(question, low, high, answer1, answer2):

    # Stored Variable
    ERROR = "Please enter a whole number \n"

    # Keep asking until a valid number is entered
    while True:
        try:

            # Ask users age
            age = int(input(question))

            # Checking if age between 5-12
            if age < low:
                return answer1
            elif age > high:
                return answer2
            else:
                return age

        except ValueError:
            print(ERROR)


# Checker function
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
            print(f"Please answer '{question1}' or '{question2}'")


# Instructions function
def instructions():
    formatter("^", "Instructions")
    print("The rules of the game will go here")
    print()


# Random question generator function
def random_generator(lists, asking, num1, num2, num3, rounds):
    # Variables
    score = 0

    # Plays 5 rounds
    for round_number in range(rounds):

        # number of rounds
        formatter("~", f"Round {round_number + 1}")

        # Mixes up the list so different question is chosen
        random.shuffle(lists)

        # Asks the user the question
        question = input(asking.format(lists[0][num2])).title()

        # if user got it right
        if question == lists[0][num1] or question == lists[0][num3]:
            answer = "right! Congratulations!"
            sign = "!"
            score += 1

        # if user got it wrong
        else:
            answer = f"wrong, the correct answer was '{lists[0][num1]}'. Try again next time! "
            sign = "#"

        # printing if user was right or wrong
        print()
        formatter(sign, f"You got it {answer}")
        print()

        # To avoid questions being repeated, each question is removed once displayed
        lists.pop(0)

    formatter("=", f"You got {score} out of {rounds}")

    if score < 5:
        responce = "You need to learn your Maori numbers!"
    if score == 10:
        responce = "Well done! You got them all right!"
    else:
        responce = "Good job!"

    return responce


# Formatting statement function
def formatter(symbol, text):

    # Creating formatted statement
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    # printing formatted statement
    print(top_bottom)
    print(formatted_text)
    print(top_bottom)
    print()


# Welcome screen
formatter("-", "Welcome to the Māori numbers quiz")


# User name
name = input("What is your name? ").title()
print()

# user age
user_age = num_checker(f"What is your age, {name}? ", 5, 12, "young", "old")
print()

# Checking if user is too old or to young
if user_age == "young" or user_age == "old":
    print(f"Sorry {name}, you are too {user_age} to play")
    quit()

# Yes/No checker
played_before = checker("Have you played this quiz before (y/n)? ", "yes", "no")
print()

# Instructions displayed
if played_before == "No":
    instructions()

# Asking user if they want easy mode or hard mode
hard_easy = checker("Do you want to play hard mode (h) or easy mode (e)? ", "hard", "easy")
print()

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

# Numbers of rounds user will play
number_of_rounds = 10

# Easy or hard mode printed
formatter("+", f"{hard_easy} Mode:")

# User plays easy mode
if hard_easy == "Easy":
    final_score = random_generator(numbers, "What is {} in English? ",
                                   0, 2, 1, number_of_rounds)
# User plays hard mode
else:
    final_score = random_generator(numbers, "What is {} in Maori? ",
                                   2, 0, 0, number_of_rounds)

# printing final score and farewell

formatter("*", f"Nice Job! Farewell {name} ")





