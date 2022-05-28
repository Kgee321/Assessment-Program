"""Base component -- Version 2
Adding user's name in places to make the user feel appreciated
Put in formatter function to make important statements stand out
Add in the round number into random_generator function
Adding in instructions
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

            # Checking if age between the boundary's
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

        # Asks the user the question
        answer = input(question_text).lower()

        # If user answers first response
        if answer == question1 or answer == question1[0]:
            answer = question1.title()
            return answer

        # If user answers second response
        elif answer == question2 or answer == question2[0]:
            answer = question2.title()
            return answer

        # otherwise - show error
        else:
            print(f"Please answer '{question1}' or '{question2}'")


# Instructions function
def instructions():
    formatter("^", "Instructions")
    print('Welcome to my Te Rao Māori quiz. Here some rule and instructions '
          'you will need to know before playing. Below, you will get asked if '
          'you want to play Easy mode or Hard mode. For hard mode, type "H" '
          'or "Hard," while for easy mode, type "E" or "Easy."')
    print()
    print('Easy mode means I will give you a Māori number and you will type '
          'in its English translations. You can answer used numbers or words '
          'to respond. For example, if I asked you what “kore” is in English, '
          'you will want to enter “0” or “Zero” as that is the correct answer. '
          'If you want to respond with a word, keep in mind that it must be spelt '
          'correctly, or it will be incorrect.')
    print()
    print('Hard mode means I will give you an English number '
          'and you will have to type in its Māori translations. For example, '
          'if I ask you what “0” means in Māori, you will want to enter “Kore” '
          'as that is the correct answer Remember to spell the Mori word correctly; '
          'otherwise, it will be incorrect.')
    print()
    print('My quiz has 10 questions that you must answer correctly in order to '
          'receive one point. If you get it wrong, you will not get a point and '
          'I will tell you the correct answer so you can get it right next time. '
          'If you do not know the answer, just take a guess as you may have it right! '
          'At the end, I will show you your final score out of 10 points. '
          'Can you answer all the questions correctly?')


# Random question generator function
def random_generator(lists, asking, num1, num2, num3, rounds):
    # Variables
    score = 0

    # Rounds played
    for round_number in range(rounds):

        # Number of rounds
        formatter("~", f"Round {round_number + 1}")

        # Mixes up the list so different question is chosen
        random.shuffle(lists)

        # Asks the user the question
        question = input(asking.format(lists[0][num2])).title()

        # If user got it right
        if question == lists[0][num1] or question == lists[0][num3]:
            answer = "right! Congratulations!"
            sign = "!"
            score += 1

        # If user got it wrong
        else:
            answer = f"wrong, the correct answer was '{lists[0][num1]}'. Try again next time! "
            sign = "#"

        # Printing if user was right or wrong
        print()
        formatter(sign, f"You got it {answer}")
        print()

        # To avoid questions being repeated, each question is removed once displayed
        lists.pop(0)

    # Score printed
    formatter("=", f"You got {score} out of {rounds}")

    # If less than half correct
    if score < rounds/2:
        response = f"Good start! I recommend you do some more practise!"

    # If all questions correct
    elif score == rounds:
        response = "Well done! You got them all right!"

    # If any other amount right
    else:
        response = "Good job!"

    return response


# Formatting statement function
def formatter(symbol, text):

    # Creating formatted statement
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    # Printing formatted statement
    print(top_bottom)
    print(formatted_text)
    print(top_bottom)
    print()


# Welcome screen
formatter("-", "Welcome to the Māori numbers quiz")

# User name
name = input("What is your name? ").title()
print()

# User age
user_age = num_checker(f"What is your age, {name}? ", 8, 14, "young", "old")
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

# Easy or hard mode printed
formatter("+", f"{hard_easy} Mode:")

# User plays easy mode
if hard_easy == "Easy":
    final_score = random_generator(numbers, "What is {} in English? ", 0, 2, 1, 10)

# User plays hard mode
else:
    final_score = random_generator(numbers, "What is {} in Maori? ", 2, 0, 0, 10)

# Printing feedback and farewell
formatter("*", f"{final_score} Farewell {name} ")





