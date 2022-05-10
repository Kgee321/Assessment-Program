"""Component 4 (Random Question) -- Easy mode -- Version 1
Removing testing loop
limiting amount of Maori numbers to 4 number for testing
Turn print statement into a question
Checking if user got the answer correct using an if statement
Asking 4 questions
Written by Katelyn Gee
Created 9/05/2022"""

import random

# Limiting Maori number list to Tahi for to test code efficiently
maori_numbers = ["Tahi", "Rua", "Toru", "Wha"]

# Asking 4 questions
for i in range(4):

    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Asking the user for the english translation of random Maori number
    question = int(input(f"What is {maori_choice} in English? "))

    # Checking if the user got the answer correct
    if maori_choice == "Tahi" and question == 1 or \
            maori_choice == "Rua" and question == 2 or \
            maori_choice == "Toru" and question == 3 or \
            maori_choice == "Wha" and question == 4:
        print("You got it correct!")
    else:
        print("You got it wrong")
