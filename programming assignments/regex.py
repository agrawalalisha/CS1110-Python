# Alisha Agrawal (aa3se)
"""
defines several variables containing compiled regular expressions
"""
import re

# matches one of more non-whitespace characters
nospace = r"[^\s][\S]*"
nospace = re.compile(nospace)

# matches text beginning and ending with a ", with no internal ",
# where the first and last character inside the quotes are not spaces.
quotation = r'"[^\s][a-z ]+[^"][^\s]"'
quotation = re.compile(quotation)

# matches pairs of numbers, separated by a space, comma, or both
twonum = r"(-?\d+(\.\d+)?)(,|\s|,\s)(-?\d+(\.\d+)?)"
twonum = re.compile(twonum)
