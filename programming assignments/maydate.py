# Alisha Agrawal (aa3se)
"""
The function takes in two people's ages
and returns true if it is creepy
for them to date
"""


# returns if two ppl can date
def creepy(age1, age2):
    minAge = int(age1 / 2) + 7
    maxAge = age1 * 2 - 13
    return age2 < minAge or age2 > maxAge
