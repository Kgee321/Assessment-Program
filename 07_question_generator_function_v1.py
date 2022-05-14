"""Component 4 (Random Generator) -- Function -- Version 1
Converting 06_v5 into a recyclable function so I able to use any list
of words for my code
Also changing the numbers list that it does not need to contain
integer but can contain strings.
This means I am able to swap the language around for easy and hard mode
Written by Katelyn Gee
Created 10/05/2022"""

import random


def random_generator(list1, list2, asking, rounds):
    # Variables
    score = 0

    for i in range(rounds):

        # Random Maori number chosen
        choice = random.choice(list1)

        # Asking the user for the english translation of random Maori number
        question = input(asking.format(choice)).title()

        # Finding the correct answer to the question
        correct_answer = list2[list1.index(choice)]

        # Loop to check if user is correct
        for num in range(len(list1)):

            # User got it right, loop breaks
            if choice == list1[num] and question == list2[num]:
                score += 1
                answer = "right! Congratulations!"
                break

            # User got it wrong, loop continues
            else:
                answer = f"wrong. The correct answer was {correct_answer}"

        # Removing chosen numbers to avoid questions repeating
        list1.remove(choice)
        list2.remove(correct_answer)

        # Printing if user is right or wrong
        print(f"You got it {answer}")
        print()
    return score


# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
english_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Calling on function
final_score = random_generator(english_numbers, maori_numbers,
                               "What is {} in Maori? (Answer only using numbers) ", 10)

# Telling user there score
print()
print(f"You got {final_score} out of 10 correct")
