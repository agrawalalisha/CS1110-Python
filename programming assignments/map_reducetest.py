# Alisha Agrawal (aa3se)
"""
two functions: mymap and myreduce
"""

def mymap(func, lst):
    """
    returns a list containing the result of
    applying a function to each element of that list
    :param func: any function with one parameter
    :param lst: any list for the function to be applied on
    :return: list with function applied to each element of list
    """
    newlst = list()
    for i in range(len(lst)):
        newlst.append(func(lst[i]))
    return newlst

def myreduce(func, lst):
    """
    using a function repeatedly to combine all
    elements of the list into a single value

    :param func: two-argument function
    :param lst: any list for the function to be applied on
    :return: an computed integer
    """
    ans = lst[0]
    final = 0
    for i in range(len(lst) - 1):
        ans = func(ans, lst[i + 1])
        final = ans
    return final

x = [3, -1, 4, -1, 5]

print(x)
print(myreduce(pow, x))
print(mymap(abs, x))


def wiggle(a, b):
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    c = b % a
    if c == 0:
        return a + b
    return c


def waggle(a):
    if a < 0:
        return -2 * a
    else:
        return 2 * a + 1


x = [3, -1, 4, -1, 5, -9, 2, -6, 5, -3, 5]

print(myreduce(wiggle, x))
print(mymap(waggle, x))
print(myreduce(wiggle, mymap(waggle, x)))
print(x)
