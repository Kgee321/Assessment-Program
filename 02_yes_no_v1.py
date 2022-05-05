"""Component 2 (yes/no checker) -- version 1
Asking user if they have played before and printing their answer
Written by Katelyn Gee
Created on the 5/05/2022
"""

# Ask the user if they have played before
show_instructions = input("Have you played this quiz before? ")

# if they say yes, output 'program continues'
if show_instructions == "yes":
    print("Program continues")

# if they say no, out 'instructions displayed'
elif show_instructions == "no":
    print("Display instructions")

# otherwise - show error
else:
    print("Please answer 'yes' or 'no'")
