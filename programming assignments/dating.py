# Alisha Agrawal (aa3se)
"""
This program prompts the user for their age
and returns the age range for people they can date
according to an old folk rule.
"""

# ask the user for their age
age = input("How old are you? ")
age = int(age)

# print the age range of people they can date
min = int(age/2)+7
max = age*2-13
print("You can date people between", min, "and", max, "years old")
