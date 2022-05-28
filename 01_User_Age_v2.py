"""Component 1 (User Age) -- Version 2
Use try/accept and pull error message out of the loop
Written by Katelyn Gee
Created on 3/05/2022
"""

# Variables
ERROR = "Please enter a whole number \n"
valid = False

# Keep asking until a valid number is entered
while not valid:
    try:

        # Ask users age
        user_age = int(input("What is your age, <name>? "))

        # If user younger than 8
        if user_age < 8:
            print(f"{user_age} is too young for you to play")
            print("Program ends")
            break

        # If user older than 14
        elif user_age > 14:
            print(f"{user_age} is too old for you to play")
            print("Program ends")
            break

        # Otherwise
        else:
            print(f"You are {user_age} years old")
            print("Program continues")
            valid = True

    # If a string or float entered, game does not crash
    except ValueError:
        print(ERROR)





