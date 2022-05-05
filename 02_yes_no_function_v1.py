"""Component 2 (yes/no checker) -- function v1
based on 01_yes_no_v1 but in a recyclable yes/no function
Changing show_instructions to answer to make it more generic
Written by Katelyn Gee
Created on the 5/05/2022
"""


# function goes here..
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
            print("Program continues")

        # if they say no, out 'instructions displayed'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
            print("Display instructions")

        # otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Main routine goes here...
show_instruction = yes_no("Have you played this quiz before? ")
print(f"You entered '{show_instruction}'")
