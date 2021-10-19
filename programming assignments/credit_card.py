# Alisha Agrawal (aa3se)


def check(num):
    """
    returns true if the integer represents a valid credit card number

    :param num: a positive credit card number
    :return: whether or not pos qualifies as a credit card number or not
    """
    string = str(num)
    length = len(str(num))
    flip = string[length::-1]  # reverses string to start with right-most digit
    num = list(map(int, str(flip)))  # turns string digits into integers in a list

    sums = sum(num[0::2])  # sums every other digit, including right-most digit

    for i in range(1, len(num), 2):
        num[i] = num[i] * 2  # doubles remaining digits

    doubles = list(num[1::2])
    for i in range(len(doubles)):
        doubles[i] = sum(map(int, str(doubles[i])))  # splits each element in the list into their comprising digits

    ans = sums + sum(doubles)  # adds part one and part two together

    if ans % 10 == 0:  # checks if sum of two parts is multiple of 10
        return True
    else:
        return False
