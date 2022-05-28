"""Component 1 (User Age) -- Version 4
Removing the parts of the code I added for testing including loops and
extra print statement that were in version 3 so it is ready to be
pasted into the 00_MQ_Base_v1.
Also making the code quit/stop if user is too young or old.
Written by the Katelyn
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

            # Checking if age between 5-12
            if age < low:
                return answer1
            elif age > high:
                return answer2
            else:
                return age

        except ValueError:
            print(ERROR)


# user age
user_age = str(num_checker("What is your age, <name>? ", 8, 14,
                           "young. You should try an easier Maori quiz",
                           "old. You should try a harder  Maori quiz"))
print()

# Checking if user is too old or too young
if user_age[0] == "y" or user_age[0] == "o":
    print(f"Sorry, you are too {user_age}.")
    quit()
