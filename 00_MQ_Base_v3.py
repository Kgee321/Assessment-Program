"""Base component -- Version 3
Adding in the quiz instructions and other edits
Changing random_generator to questions as it suits the code more
Written by Katelyn Gee
created on 21/05/2022
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

    # How to play my game:
    formatter("^", "Instructions")
    print("Welcome to my Te Rao Māori quiz.\n")
    print()
    print("Easy mode means you enter the English translation to the Māori number given.\n")
    print("In hard mode, you do the opposite.")
    print()
    print("My quiz is 10 questions long and I will give your final score out of 10 at the end.")
    print()
    print("Good Luck!!")


# Random question generator function
def questions(lists, asking, num1, num2, num3, rounds):
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
        response = f"You need to do some more practise!"
    if score == 10:
        response = "Well done! You got them all right!"
    else:
        response = "Good job! Try to get them all right next time!"

    return response


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
numbers = [["1", "One", "Tahi"], ["2", "Two", "Rua"],
           ["3", "Three", "Toru"], ["4", "Four", "Wha"],
           ["5", "Five", "Rima"], ["6", "Six", "Ono"],
           ["7", "Seven", "Whitu"], ["8", "Eight", "Waru"],
           ["9", "Nine", "Iwa"], ["10", "Ten", "Tekau"]]

# Easy or hard mode printed
formatter("+", f"{hard_easy} Mode:")

# User plays easy mode
if hard_easy == "Easy":
    final_score = questions(numbers, "What is {} in English? ", 0, 2, 1, 10)

# User plays hard mode
else:
    final_score = questions(numbers, "What is {} in Maori? ", 2, 0, 0, 10)

# printing final score and farewell
formatter("*", f"{final_score} Farewell {name} ")





