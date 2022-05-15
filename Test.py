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
    question1 = input(f"What is {choice} in {language}? ").lower()

    # All possible winning outcomes
    if choice == test_list[0] and question1 == "1" or choice == "Rua" and question1 == "2" or choice == "Toru" and question1 == "3" or choice == "Wha" and question1 == "4" or choice == "1" and question1 == "Tahi" or choice == "2" and question1 == "Rua" or choice == "3" and question1 == "Toru" or choice == "4" and question1 == "Wha":
        print("You got it right!")
    else:
        print("You got it wrong!")


def test_three():
    text = "Hello world"
    sides = "$" * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = "*" * len(formatted_text)

    print(top_bottom)
    print(formatted_text)
    print(top_bottom)

test_three()
