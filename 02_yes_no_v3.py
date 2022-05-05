"""Component 2 (yes/no checker) -- version 3
Puts the code created in v2 into a loop to make testing easier and more efficient.
Written by Katelyn Gee
Created on the 5/05/2022
"""

# loop for testing
show_instructions = ""
while show_instructions != "x":

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

    print(f"You entered '{show_instructions}'")
