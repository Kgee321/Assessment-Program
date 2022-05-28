"""Component 2 (yes/no checker) -- function v2
Making version 1 function more recyclable so it can be used for different responses
that are not just yes and no.
Also changing function name to be more generic
Written by Katelyn Gee
Created on the 5/05/2022
"""


# checker functions
def checker(question_text, question1, question2):
    while True:

        # Asking question
        answer = input(question_text).lower()

        # If user input is the same as first response
        if answer == question1 or answer == question1[0]:
            answer = question1.title()
            return answer

        #  If user input is the same as second response
        elif answer == question2 or answer == question2[0]:
            answer = question2.title()
            return answer

        # Otherwise - show error
        else:
            print(f"Please answer with '{question1}' or '{question2}'")


# Main routine
show_instruction = checker("Have you played this quiz before? ", "yes", "no")

# Print answer
print(f"You entered '{show_instruction}'")
