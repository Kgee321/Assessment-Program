"""Component 2 (yes/no checker) -- function v2
Making version 1 function more recyclable so it can be used for different responses
that are not just yes and no.

Written by Katelyn Gee
Created on the 5/05/2022
"""


# function goes here..
def yes_no(question_text, question1, question2):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'program continues'
        if answer == question1 or answer == question1[0]:
            answer = question1.title()
            return answer
            print("Program continues")

        # if they say no, out 'instructions displayed'
        elif answer == question2 or answer == question2[0]:
            answer = question2.title()
            return answer
            print("Display instructions")

        # otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Main routine goes here...
show_instruction = yes_no("Have you played this quiz before? ", "yes", "no")
print(f"You entered '{show_instruction}'")
