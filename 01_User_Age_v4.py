"""Component 1 (User Age) -- Version 4
Changing Version 2 into a function
Also need to change user_name to the more generic variable name 'age'
and change the condition of the number comparison into the
loop to make the function recyclable
Removing valid variable to make code shorter
Function repeated for testing
Written by Katelyn Gee
Created on 4/05/2022
"""


def num_checker(question, low, high, answer1, answer2):

    # Stored Variable
    ERROR = "Please enter a whole number \n"

    # Keep asking until a valid number is entered
    while True:
        try:

            # Ask users age
            age = int(input(question))

            # Checking if age in the right boundary's
            if age < low:
                return answer1
            elif age > high:
                return answer2
            else:
                return age

        except ValueError:
            print(ERROR)


# Repeating code for testing purposes
valid = ""
while valid != "x":
    user_age = num_checker("What is your age, <name>? ", 8, 14,
                           "too young -- program ends",
                           "too old -- program ends")
    print(f'You are {user_age}')












