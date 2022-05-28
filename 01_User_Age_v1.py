"""Component 1 (User Age) -- Version 1
Asking for users age
Not allowing the program to continue if user
older than 12 or younger than 5
Although, code does crash when a string or float is entered
<name> will be replaced with users name later in the code
Written by Katelyn Gee
Created on 3/05/2022
"""

# Ask users age
user_age = int(input("What is your age, <name>? "))

# If user age lower than 8
if user_age < 8:
    print(f"{user_age} is too young for you to play")
    print("Program ends")

# If user age higher than 14
elif user_age > 14:
    print(f"{user_age} is too old for you to play")
    print("Program ends")

# Otherwise -- User is the right age to play
else:
    print(f"You are {user_age} years old")
    print("Program continues")





