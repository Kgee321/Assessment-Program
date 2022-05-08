""" Component 3 (Hard/Easy mode)
I am going to use the recyclable checker function I created in yes_no_function_v2
to make sure the user gives the right response for easy mode or hard mode.
Also looping the function for testing
Written by Katelyn Gee
created on the 7/05/2022"""


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


# Main routine goes here...
while "y" != "x":
    hard_easy = checker("Do you want to play hard mode (h) or easy mode (e)? ", "hard", "easy")
    print(f"You are playing '{hard_easy}' mode")
    print()
