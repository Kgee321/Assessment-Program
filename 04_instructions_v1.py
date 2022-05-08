"""Component 2 (instructions) -- Version 1
Took function from 03_v2 as the basis for this new function which
incorporates both checker and show instructions
Written by Katelyn Gee
Created by 7/05/2022"""


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


# Main routine goes here...
played_before = checker("Have you played this quiz before? ", "yes", "no")

if played_before == "No":
    instructions()
else:
    print("Program continues")


