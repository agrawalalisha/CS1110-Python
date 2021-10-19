# Alisha Agrawal (aa3se)
"""
This program computes
a cumulative GPA
"""

fin_gpa = 0
fin_credits = 0


# adds gpa and credits to existing values
def add_course(new_gpa, new_credits=3):
    global fin_gpa
    global fin_credits
    fin_gpa = (((fin_gpa*fin_credits) + (new_gpa*new_credits))/(fin_credits + new_credits))
    fin_credits = fin_credits + new_credits


# returns new gpa
def gpa():
    return fin_gpa


# returns new credit total
def credit_total():
    return fin_credits
