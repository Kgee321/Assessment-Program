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

        # Checking if age between 5-12
        if user_age < 5:
            print(f"{user_age} is too young for you to play")
            print("Program ends")
            break
        elif user_age > 12:
            print(f"{user_age} is too old for you to play")
            print("Program ends")
            break
        else:
            print(f"You are {user_age} years old")
            print("Program continues")
            valid = True

    except ValueError:
        print(ERROR)





