# Alisha Agrawal (aa3se)
"""
This program plays a simple
number guessing game
between the user
"""

import random

ask = int(input("What should the answer be? "))
guess = int(input("How many guesses? "))
num = int(input("Guess a number: "))
x = 1

if ask == -1:
    ask = random.randrange(1, 101)

while x <= guess and num != ask:
    x += 1
    if x > guess:
        print("You lose; the number was", str(ask) + ".")
    elif num > ask:
        print("The number is lower than that.")
        num = int(input("Guess a number: "))
    elif num < ask:
        print("The number is higher than that.")
        num = int(input("Guess a number: "))

if num == ask:
    print("You win!")
