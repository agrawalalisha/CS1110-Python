# Alisha Agrawal (aa3se)


def check(num):
    """
    returns true if the integer represents a valid credit card number

    :param num: a positive credit card number
    :return: whether or not pos qualifies as a credit card number or not
    """
    num = list(map(int, str(num)))  # turns string digits into integers in a list
    sums = sum(num[-1:len(num):2])  # sums every other digit, including right-most digit
    print(sums)
    for i in range(len(num), len(num), 2):
        num[i] = num[i] * 2  # doubles remaining digits
    print(num)
    doubles = list(num[1::2])
    print(doubles)
    for i in range(len(doubles)):
        doubles[i] = sum(map(int, str(doubles[i])))  # splits each element in the list into their comprising digits
        print(doubles[i])

    ans = sums + sum(doubles)  # adds part one and part two together
    print(ans)
    if ans % 10 == 0:  # checks if sum of two parts is multiple of 10
        return True
    else:
        return False

if check(240):
    print('GOOD: 240 is valid')