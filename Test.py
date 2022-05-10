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


def test_three(language, test_list):
    choice = random.choice(test_list)
    question1 = input(f"What is {choice} in {language}? ").lower()

    # All possible winning outcomes
    for i in range(4):
        if choice == test_list[i] and question1 == str(i):
            print("Correct")
            answer = "Yes"
            return answer




# test_three("english", ["Tahi", "Rua", "Toru", "Wha"])
# test_three("Te Rao", [1, 2, 3, 4])

def test_four(lists):
    choice = random.choice(lists)
    question = input(f"What is {choice}? ").lower()
    if len(question) > 2:
        print("Answer is letters")
        print(lists[question])
        print(question)
        if lists[choice] == 4 and question == "toru": # or question1 == "Rua" and choice == 2:
            print("Working")
    elif len(question) < 2:
        print("Answer is numbers")
        for i in range(4):
            print(question)
            number = i + 1
            print(number)
            print(choice)
            print(lists[i])
            if question == str(number) and choice == lists[i]:
                print("Yes")
                break
            else:
                print("No")



test_four(["Tahi", "Rua", "Toru", "Wha"])
test_four([1,2,3,4])




