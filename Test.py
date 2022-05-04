"""This is a space where I can test any code I am unsure of
Katelyn Gee
3/05/2022"""

print("Hello World")


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


test_one()
