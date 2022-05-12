"""Component 4 (Random Generator) -- Version 5
Editing 06_v4.
Changing code so that numbers_list can contain strings instead of only numbers
Also adding feedback to the user by telling them the correct answer when they get it wrong.
Written by Katelyn Gee
Created 10/05/2022"""

import random

# Variables
score = 0

# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for number in range(10):

    # Round number
    rounds = number + 1
    print(f"{'--' * 5} Round {rounds} {'--' * 5}")
    print()

    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Asking the user for the english translation of random Maori number
    question = input(f"What is {maori_choice} in English? (Answer using numbers) ")

    # Loop to check if user is correct
    correct_answer = str(numbers_list[maori_numbers.index(maori_choice)])
    print(correct_answer)

    if question == correct_answer:
        print("Correct! Congrats")
    else:
        print("Wrong")

    maori_numbers.remove(maori_choice)


# Telling user there score
print()
print(f"You got {score} out of 10 correct")
