# review for exam1
"""

"""

"""
def rem(a, b):
    return (a ** b) % 7


print(rem(7, 7))

"""

"""
def norm_num(num):
    float1 = float(num)
    int1 = int(float1)
    if (float1 == int1):
        return int1
    else:
        return float1


print(norm_num(2))
print(norm_num(2.0))
print(norm_num(2.3))
print(norm_num('2.0'))

"""
""""
age = int(input("How old are you? "))
year = int(input("What year were you born? "))
turning = 2017 - year

if turning == age:
    print("You've already had a birthday this year!")
elif turning - 1 == age:
    print("Your birthday is coming up!")
else:
    print("Shouldn't you be either", turning - 1, "or", turning, "!")

"""
person = ''

def invite(human):
    global person
    person = person+" ,"+human
    print(person)

invite("sally")
invite("franklyn")


print(100*'%')