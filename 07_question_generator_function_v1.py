"""Component 4 (Random Generator) -- Function -- Version 1
Converting 06_v5 into a recyclable function so I able to use any list
of words for my code
Also changing the numbers list that it does not need to contain
integer but can contain strings.
This means I am able to swap the language around for easy and hard mode
Written by Katelyn Gee
Created 10/05/2022"""

import random


def random_generator(list1, list2, language):

    # Variables
    score = 0

    for number in range(10):

        # Round number
        rounds = number + 1
        print(f"{'--' * 5} Round {rounds} {'--' * 5}")
        print()

        # Random Maori number chosen
        choice = random.choice(list1)

        # Asking the user for the english translation of random Maori number
        question = input(f"What is {choice} in {language}? (Answer using numbers) ").title()

        # Loop to check if user is correct
        for num in range(len(maori_numbers)):

            # User got it right, loop breaks
            if choice == list1[num] and question == list2[num]:
                score += 1
                answer = "right!"
                list1.remove(choice)
                list2.remove(question)
                break

            # User got it wrong, loop continues
            else:
                answer = "wrong"

        # Printing if user is right or wrong
        print(f"You got it {answer}")
        print()
    return score


# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Calling on function
final_score = random_generator(maori_numbers, numbers_list, "English")

# Telling user there score
print()
print(f"You got {final_score} out of 10 correct")



