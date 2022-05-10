"""Component 4 (Random Question) -- Easy mode -- Version 1
Adding in the rest of the Te Rao numbers
Also adding score and rounds
Looping question so 5 questions/rounds play
Removing Maori numbers once they have been used so that questions are not repeated
Written by Katelyn Gee
Created 9/05/2022"""

import random

# Variables
score = 0

# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]

for i in range(10):
    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Round number
    rounds = i + 1
    print(f"{'--' * 5} Round {rounds} {'--' * 5}")

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
        answer = "right!"
        score += 1
        maori_numbers.remove(maori_choice)
    else:
        answer = "wrong"

    print(f"You got it {answer}")

print(f"You got {score} out of 10 points")
