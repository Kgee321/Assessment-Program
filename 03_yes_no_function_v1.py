"""Component 2 (yes/no checker) -- function v1
Based on 01_yes_no_v3 but in a recyclable yes/no function
Changing show_instructions to answer to make it more generic
Changing the while statement so question repeats if wrong input
Written by Katelyn Gee
Created on the 5/05/2022
"""


# yes/no functions
def yes_no(question_text):
    while True:

        # Asking question
        answer = input(question_text).lower()

        # if answer is yes
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # if answer is no
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Main routine
show_instruction = yes_no("Have you played this quiz before? ")

# Print answer
print(f"You entered '{show_instruction}'")
