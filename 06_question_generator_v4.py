"""Component 4 (Random Question) -- Easy mode -- Version 4
Using a range loop to check if user got the answer right instead of
having the very long if statement to making code more efficient
Removing Maori numbers once they have been used so that questions are not repeated
Written by Katelyn Gee
Created 9/05/2022"""

import random

# Variables
score = 0

# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in range(10):

    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Round number
    rounds = number + 1
    print(f"{'--' * 5} Round {rounds} {'--' * 5}")
    print()

    # Asking the user for the english translation of random Maori number
    question = int(input(f"What is {maori_choice} in English? (Answer using numbers) "))

    # Loop to check if user is correct
    for num in range(len(maori_numbers)):

        # User got it right, loop breaks
        if maori_choice == maori_numbers[num] and question == numbers_list[num]:
            score += 1
            answer = "right!"
            maori_numbers.remove(maori_choice)
            numbers_list.remove(question)
            break

        # User got it wrong, loop continues
        else:
            answer = "wrong"

    # Printing if user is right or wrong
    print(f"You got it {answer}")
    print()

# Telling user there score
print()
print(f"You got {score} out of 10 correct")
