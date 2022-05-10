""""Trying to get this stupid code to work
What if I had function that asked the questions, then it went back to yes/no checker"""


import random

# Variables
score = 0

# List of Maori words up to 10
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]
amount_of_numbers = len(maori_numbers)

for number in range(5):

    # Random Maori number chosen
    maori_choice = random.choice(maori_numbers)

    # Round number
    rounds = number + 1
    print(f"{'--' * 5} Round {rounds} {'--' * 5}")

    # Asking the user for the english translation of random Maori number
    question = int(input(f"What is {maori_choice} in English? (Answer using numbers) "))

    # Loop to check if user is correct
    for num in range(len(maori_numbers)):
        new_num = num + 1
        print(maori_choice)
        print(maori_numbers[num])
        print(question)
        print(new_num)
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
            print("Continue")

    # Removes chosen maori numbers from list so questions do not repeat
    maori_numbers.remove(maori_choice)

    # Printing if user is right or wrong
    print(f"You got it {answer}")

# Telling user there score
print()
print(f"You got {score} out of 5 points")

