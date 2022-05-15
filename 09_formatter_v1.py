"""Component 5 - statement formatter v1
Written by Katelyn Gee
Created 15/05/2022
"""

# Creating formatted statement
symbol = "*"
text = "Hello world"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

# printing formatted statement
print(top_bottom)
print(formatted_text)
print(top_bottom)
