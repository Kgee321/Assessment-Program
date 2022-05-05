"""Component 2 (instructions) -- Version 1
Took function from 03_v2 as the basis for this new function which
incorporates both checker and show instructions"""

# function goes here..
def checker(question_text, question1, question2):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'program continues'
        if answer == question1 or answer == question1[0]:
            answer = question1.title()


        # if they say no, out 'instructions displayed'
        elif answer == question2 or answer == question2[0]:
            answer = question2.title()
            return answer
            print("Display instructions")

        # otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Main routine goes here...
show_instruction = checker("Have you played this quiz before? ", "yes", "no")
print(f"You entered '{show_instruction}'")
