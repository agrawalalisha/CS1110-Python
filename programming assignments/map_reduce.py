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
