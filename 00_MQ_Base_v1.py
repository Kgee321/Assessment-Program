"""Base component -- Version 1
Welcome screen created here
Adding each component as they are added
Not much editing done to the code
Written by Katelyn Gee
created on 3/05/2022
"""


# number checker
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
            print(f"Please answer '{question1}' or '{question2}'")


# Instructions functions
def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")


# Welcome screen
print(f"{'--'*10} Maori Numbers 1 to 10 Quiz {'--'*10}")
print()

# User name
name = input("What is your name? ").title()
print(f"Welcome {name}") # Remove in next version -- delete this
print()

# user age
user_age = num_checker(f"What is your age, {name}? ", 5, 12, "young", "old")

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

# Hard mode or easy mode
hard_easy = checker("Do you want to play hard mode (h) or easy (e)? ", "easy", "hard")









