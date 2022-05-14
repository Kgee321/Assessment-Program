"""Component 4 (Random Generator) -- Version 1
Chooses a random Te Rao number and prints it in a question format
Testing if I have chosen a random Maori number correctly
It works!
Written by Katelyn Gee
Created 9/05/2022"""

import random

# List of the Maori numbers up to 10
maori_numbers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

# Testing if a different random number is chosen each time (20 times)
for i in range(20):
    maori_choice = random.choice(maori_numbers)
    question = input(f"What is {maori_choice} in English? ")

