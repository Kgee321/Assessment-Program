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
    ERROR = f"Please enter a whole number\n"

    # Keep asking until a valid number is entered
    while True:
        try:

            # Ask users age
            age = int(input(question))

            # Checking if age meets required boundary
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

    # Keep asking until valid input entered
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if user input is the same as first response
        if answer == question1 or answer == question1[0]:
            answer = question1.title()
            return answer

        # if user input is the same second response
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
    print("Easy mode means you enter the English translation to "
          "the Māori number given.\n")
    print("In hard mode, you do the opposite.\n")
    print("My quiz is 10 questions long and I will give your final "
          "score out of 10 at the end.\n")
    print("Good Luck!!\n")


# Random question generator function
def questions(lists, asking, num1, num2, num3, rounds):

    # Variables
    score = 0

    # Plays 5 rounds
    for round_number in range(rounds):

        # Number of rounds
        formatter("~", f"Question {round_number + 1}")

        # Mixes up the list so different question is chosen
        random.shuffle(lists)

        # Asks the user the question
        question = input(asking.format(lists[0][num2])).title()

        # If user is right
        if question == lists[0][num1] or question == lists[0][num3]:
            answer = "right! Congratulations!"
            sign = "!"
            score += 1

        # If user misspells the word
        elif lists[0][num1][0] == question[0]:
            answer = "so close, but the word was misspelt. " \
                     f"The correct spelling was '{lists[0][num1]}' "
            sign = "#"

        # If user is wrong
        else:
            answer = f"so close! The correct answer was '{lists[0][num1]}'. " \
                     "Try again next time! "
            sign = "#"

        # Printing if user is right, wrong or misspelt
        print()
        formatter(sign, f"You are {answer}")
        print()

        # Removing used questions to avoid them repeating
        lists.pop(0)

    # Final score
    formatter("=", f"You got {score} out of {rounds}")

    # Giving user feedback
    if score <= 5:
        response = "Good start! I recommend you do some more practise!"
    elif score == 10:
        response = "Congratulations!! You got them all right!"
    else:
        response = "Good job! You did well!"

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
formatter("-", "Haramai! Welcome to my Māori numbers quiz")

# User name
name = input("What is your name? ").title()
print()

# User age
user_age = str(num_checker(f"What is your age, {name}? ", 8, 14,
                           "young. You should try an easier Maori quiz",
                           "old. You should try a harder Maori quiz"))
print()

# Checking if user is too old or to young
if user_age[0] == "y" or user_age[0] == "o":
    print(f"Sorry, you are too {user_age}.")
    quit()

# Yes/No checker
play_before = checker("Have you played this quiz before (y/n)? ", "yes", "no")
print()

# Instructions displayed
if play_before == "No":
    instructions()

# Asking user if they want easy mode or hard mode
hard_easy = checker("Do you want to play hard mode (h) or easy mode (e)? ",
                    "hard", "easy")
print()

# List of English and Maori numbers
numbers = [["1", "One", "Tahi"], ["2", "Two", "Rua"],
           ["3", "Three", "Toru"], ["4", "Four", "Wha"],
           ["5", "Five", "Rima"], ["6", "Six", "Ono"],
           ["7", "Seven", "Whitu"], ["8", "Eight", "Waru"],
           ["9", "Nine", "Iwa"], ["10", "Ten", "Tekau"]]

# Mode printed
formatter("+", f"{hard_easy} Mode:")

# User plays easy mode
if hard_easy == "Easy":
    final_score = questions(numbers, "What is {} in English? ", 1, 2, 0, 10)

# User plays hard mode
else:
    final_score = questions(numbers, "What is {} in Maori? ", 2, 0, 0, 10)

# Feedback and goodbye statement
formatter("*", f"{final_score} Haere rā {name} ")
