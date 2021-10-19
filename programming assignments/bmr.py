# Alisha Agrawal (aa3se)
"""
This program returns
Mifflin St Jeor estimate of
the basal metabolic rate, an
estimate of the Calories consumed to
keep the body alive
"""


# returns estimate of the basal metabolic rate
def st_jeor(mass, height, age, sex):
    if sex == 'male':
        s = 5
    else:
        s = -161
    ans = ((10.0 * mass) + (6.25 * height) - (5.0 * age) + s)
    return ans
