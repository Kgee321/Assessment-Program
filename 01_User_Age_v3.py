"""Component 1 (User Age) -- Version 3
Trying to eliminate valid variable to shorten code, but the code does not end
if the user is over or under aged. This means this code may be shorter,
but it does not work to the standard it should.
Written by Katelyn Gee
Created on 4/05/2022
"""
# Variables
ERROR = "Please enter a whole number \n"
user_age = 0

# Keep asking until a valid number is entered
while not 8 <= user_age <= 14:
    try:

        # Ask users age
        user_age = int(input("What is your age, <name>? "))
        print()

    except ValueError:
        print(ERROR)

print(f"You are {user_age} years old")



