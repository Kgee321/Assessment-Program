"""Component 4 (Random Generator) -- Version 5
Using  06_v4 so it is ready to be converted into a functions
Changing code so that numbers_list can contain strings instead of only numbers
Also adding feedback to the user by telling them the correct answer when they get it wrong.
Removing te rao numbers so questions do not repeat in one game
Also changing the amount of questions asked into a while loop to make code more precise.
Also adding in score variable so the program can tell the user what their final score is
Written by Katelyn Gee
Created 10/05/2022"""

import random

# Variables
score = 0
rounds = 0

# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]

# List of English words to 10
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

while rounds != 10:

    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Asking the user for the english translation of random Maori number
    question = input(f"What is {maori_choice} in English? (Answer using numbers) ")

    # Finding the correct answer to the question
    correct_answer = numbers_list[maori_numbers.index(maori_choice)]

    # Loop to check if user is correct
    for num in range(len(maori_numbers)):

        # User got it right, loop breaks
        if maori_choice == maori_numbers[num] and question == numbers_list[num]:
            score += 1
            answer = "right! Congratulations!"
            break

        # User got it wrong, loop continues
        else:
            answer = f"wrong. The correct answer was {correct_answer}"

    # Removing chosen numbers to avoid questions repeating
    maori_numbers.remove(maori_choice)
    numbers_list.remove(correct_answer)

    # Printing if user is right or wrong
    print(f"You got it {answer}")
    print()

# Telling user their final score
print()
print(f"You got {score} out of 10 correct")
