"""Component 5 - statement formatter v2
Changing v1 into a function
Written by Katelyn Gee
Created 15/05/2022
"""


# Formatting important statements
def formatter(symbol, text):

    # Creating formatted statement
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    # Printing formatted statement
    print(top_bottom)
    print(formatted_text)
    print(top_bottom)
    print()


# Practice printing statements
formatter("-", "Welcome to Māori numbers quiz")
formatter("!", "You got it right, Congratulations")
formatter("#", "You got it wrong, Better luck next time")
formatter("=", "You got <score> out of 10")
formatter("*", "Nice Job! Farewell ")
