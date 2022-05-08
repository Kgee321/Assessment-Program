"""This is a space where I can test any code I am unsure of
Katelyn Gee
3/05/2022"""

import random


def test_one():
    age = int(input("What is your age"))
    if age > 10:
        exit()
    if age < 5:
        quit()
    else:
        print(f"You are {age}")

    name = input("What name?")
    print(f"Hi {name}")


def test_two(language, test_list):
    choice = random.choice(test_list)
    question1 = input(f"What is {choice} in {language}? (enter a number)")


    return choice


print(test_two("english", ["Tahi", "Rua", "Toru", "Wha"]))



