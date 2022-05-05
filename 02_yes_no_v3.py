"""Component 2 (yes/no checker) -- version 1
Simplifies the input by converting  it to lower case.
Also accepts y or n as abbreviations.
Prints result of user choice as well as input -- for testing
Written by Katelyn Gee
Created on the 5/05/2022
"""

# Ask the user if they have played before
show_instructions = input("Have you played this quiz before? ").lower()

# if they say yes, output 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    print("Program continues")

# if they say no, out 'instructions displayed'
elif show_instructions == "no" or show_instructions == "n":
    print("Display instructions")

# otherwise - show error
else:
    print("Please answer 'yes' or 'no'")

print(f"You entered '{show_instructions}")
