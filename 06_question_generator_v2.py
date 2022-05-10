"""Component 4 (Random Question) -- Easy mode -- Version 1
Removing testing loop
limiting amount of Maori numbers to one number for testing
Turn print statement into a question
Checking if user got the answer correct
Written by Katelyn Gee
Created 9/05/2022"""

import random

# Limiting Maori number list to Tahi for to test code efficiently
maori_numbers = ["Tahi"]

# Random Maori number chosen
maori_choice = random.choice(maori_numbers)

# Asking the user for the english translation of random Maori number
question = input(f"What is {maori_choice} in English? ")

# Checking if the user got the answer correct
if maori_choice == "Tahi" and question == "1":
    print("You got it correct!")
else:
    print("You got it wrong")

