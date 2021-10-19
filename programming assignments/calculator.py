# Alisha Agrawal (aa3se)
"""
This function evaluates strings
as mathematical expressions

"""


def binop(s):
    """
    does addition, subtraction, multiplication, and division
    :param s: the string expression being evaluated
    :return: an evaluated expression
    """
    if '+' in s:
        ix = s.find('+')
        a = int(s[0: ix])
        b = int(s[ix + 1: len(s) + 1])
        return a + b
    elif '-' in s:
        ix = s.find('-')
        c = int(s[0: ix])
        d = int(s[ix + 1: len(s) + 1])
        return c - d
    elif '*' in s:
        ix = s.find('*')
        e = int(s[0: ix])
        f = int(s[ix + 1: len(s) + 1])
        return e * f
    elif '/' in s:
        ix = s.find('/')
        g = int(s[0: ix])
        h = int(s[ix + 1: len(s) + 1])
        return g / h
