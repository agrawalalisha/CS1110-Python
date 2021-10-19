# Alisha Agrawal (aa3se)
"""
Ask the user to type a temperature in Celsius
Print the corresponding temperature in Fahrenheit
"""

# prompts user for temperature in celsius
celsius = (input("What is the temperature in Celsius? "))
celsius = int(celsius)

# converts to fahrenheit
convertFar = (celsius*1.8)+32  # formula found on rapidtables.com
print("It is", round(convertFar, 1), "degrees Fahrenheit")
