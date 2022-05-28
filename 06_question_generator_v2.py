"""Component 4 (Random Generator) -- Version 2 -- Trial 1
Removing testing loop
Checking if user got the answer correct using a long if statement
Asking 5 questions
Written by Katelyn Gee
Created 9/05/2022"""

import random

# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]

# Looping 5 times
for i in range(5):

    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Asking the user for the english translation of random Maori number
    question = int(input(f"What is {maori_choice} in English? (Answer using numbers) "))

    # Checking if the user got the answer correct
    if maori_choice == "Tahi" and question == 1 or \
            maori_choice == "Rua" and question == 2 or \
            maori_choice == "Toru" and question == 3 or \
            maori_choice == "Wha" and question == 4 or \
            maori_choice == "Rima" and question == 5 or \
            maori_choice == "Ono" and question == 6 or \
            maori_choice == "Whitu" and question == 7 or \
            maori_choice == "Waru" and question == 8 or \
            maori_choice == "Iwa" and question == 9 or \
            maori_choice == "Tekau" and question == 10:

        # If answer correct
        answer = "right!"

    else:
        # If answer wrong
        answer = "wrong"

    # Printing if user is right or wrong
    print(f"You got it {answer}")
    print()
