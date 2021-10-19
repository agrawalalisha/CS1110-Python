# Alisha Agrawal (aa3se)
"""
calculates cumulative grade
"""
running_total = {}
total_weight = {}
total_grade = {}


def assignment(kind, grade, weight=1):
    """
    add to the running total grade given a certain kind of assignment and weight
    :param kind: string, indicates which group of assignment
    :param grade: grade-value of 0 - 100
    :param weight: optional, how much weight this assignment has
    :return: nothing; adds running total grade for the given kind
    """
    global running_total
    global total_weight
    global total_grade

    if kind not in running_total:
        running_total[kind] = grade
        total_grade[kind] = 0
        total_weight[kind] = 0
    if weight > 1:
        grade *= weight
    total_grade[kind] += grade
    total_weight[kind] += weight
    running_total[kind] = total_grade[kind] / total_weight[kind]


def total(proportions):
    """
    return the cumulative grade so far based on a set of proportions of assignment kind to overall weight.
    :param proportions: dictionary of key assignment kind and overall weight
    :return: cumulative grade
    """
    final = {}
    for i in proportions:
        if i in running_total:
            final[i] = proportions[i] * running_total[i]
            print(final)
        else:
            final[i] = 0
            print(final)

    total_sum = sum(final.values())
    return total_sum
