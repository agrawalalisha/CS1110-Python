# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)
# Alisha Agrawal (aa3se) Owen Petito (otp5dp)

def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    ans = 1
    while ans * 2 <= n:
        ans = ans * 2
    return ans

marbles = 0
pick = 0

print("The Game of Nim\n")
while marbles == 0:
    marbles = int(input("The number of marbles in the pile: "))
    if marbles > 0:
        turn_choice = input("Who will start? (p or c): ")
        if turn_choice == 'p':
            turn = True
        else:
            turn = False

while marbles != 0:
    print("The pile has", marbles, "marbles in it.")
    if turn:
        can_take = marbles // 2
        if can_take < 1:
            can_take = 1
        take = 0
        while take <= 0:
            take = int(input("How many marbles to you want to take (1-" + str(can_take) + "): "))
        marbles -= take
    else:
        if pow2(marbles) * 2 == marbles + 1:
            take = 1
        else:
            target = pow2(marbles) - 1
            take = marbles - target
        if take < 1:
            take = 1
        marbles -= take
        print("The computer takes", take, "marbles.")
    turn = not turn

if turn:
    print("The player wins!")
else:
    print("The computer wins!")

