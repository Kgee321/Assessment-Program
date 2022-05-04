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
                print
            elif age > high:
                return answer2
            else:
                return age

        except ValueError:
            print(ERROR)


# Welcome screen
print(f"{'--'*10} Maori Numbers 1 to 10 Quiz {'--'*10}")
print()

# User name
name = input("What is your name?")
print(f"Welcome {name}") # Remove in next version -- delete this

# user age
user_age = num_checker("What of your age, <name>? ", 5, 12, "young", "old")

# Checking if user is too old or to young
if user_age == "young" or user_age == "old":
    print(f"Sorry, you are too {user_age} to play")
    quit()




