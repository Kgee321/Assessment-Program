"""Component 4 (Random Generator) -- Version 1
Chooses a random Te Rao number and prints it in a question format
Testing if I have chosen a random Maori number correctly
Then chooses a random English numbers and prints in a question format
Testing if I have chosen a random english number correctly
Written by Katelyn Gee
Created 9/05/2022"""

import random

# List of the Maori numbers up to 10
maori_numbers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

# Testing if a different random number is chosen each time (20 times)
for i in range(20):
    maori_choice = random.choice(maori_numbers)
    question = input(f"What is {maori_choice} in English? ")

# List of the Maori numbers up to 10
english_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Testing if a different random number is chosen each time (20 times)
for i in range(20):
    english_choice = random.choice(english_numbers)
    question = input(f"What is {english_choice} in English? ")




