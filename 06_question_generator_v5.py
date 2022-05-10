"""Component 4 (Random Question) -- Easy mode -- Version 5
I am using version 4 to use as my code because it uses less code
Making the code so questions do not repeat themselves
Written by Katelyn Gee
Created 9/05/2022"""

import random

# Variables
score = 0

# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]

for number in range(5):

    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Round number
    rounds = number + 1
    print(f"{'--' * 5} Round {rounds} {'--' * 5}")

    # Asking the user for the english translation of random Maori number
    question = int(input(f"What is {maori_choice} in English? (Answer using numbers) "))

    # Loop to check if user is correct
    for num in range(10):
        new_num = num + 1

        try:
            # User got it right, loop breaks
            if maori_choice == maori_numbers[num] and question == new_num:
                score += 1
                answer = "right!"
                break
            # User got it wrong, loop continues
            else:
                answer = "wrong"
        except ValueError:
            new_num += 1

    # Removes Maori numbers from list
    maori_numbers.remove(maori_choice)

    # Printing if user is right or wrong
    print(f"You got it {answer}")

# Telling user there score
print()
print(f"You got {score} out of 5 points")
