# Alisha Agrawal (aa3se)
"""
This program plays a simple guessing
game with the user where the user thinks
of a number and the computer guesses.

"""

print("Think of a number between 1 and 100 and I'll guess it.")
guess = int(input("How many guesses do I get? "))
count = 1
big = 101
small = 0

while count <= guess:  # checks if computer has enough guesses
    if big == small + 1:  # checks when two numbers are consecutive
        print("Wait; how can it be both higher than " +
              str(small) + " and lower than " + str(big) + "?")
        break
    user = str(input("Is the number higher, lower or the same as "
                     + str((big + small) // 2) + "? "))
    if user == "higher":
        small = (big + small) // 2  # resets to a higher minimum value
        count += 1
    elif user == "lower":
        big = (big + small) // 2  # resets to a lower maximum value
        count += 1
    elif user == "same":
        print("I won!")
        break

if count > guess:
    ans = int(input("I lost; what was the answer? "))
    if ans < small:  # checks if ans is in accordance with previous answers
        print("That can't be; you said it was higher than "
              + str(small) + "!")
    else:
        print("Well played!")
