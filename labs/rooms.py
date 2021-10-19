# (amr8xq) Audrey Risko, (aa3se) Alisha Agrawal
import robot


def square():
    r = robot.Robot(1)
    b = 1
    while r.ce() is True:
        r.e()
        b += 1
    x = b ** 2
    r.say(x)


def rectangle():
    r = robot.Robot(2)
    leng = 1
    wid = 1
    while r.ce() is True:
        r.e()
        leng += 1
    while r.cs() is True:
        r.s()
        wid += 1
    x = leng * wid
    r.say(x)


def middle():
    r = robot.Robot(3)
    leng = 1
    wid = 1
    while r.cw() is True:
        r.w()
    while r.cn() is True:
        r.n()
    while r.ce() is True:
        r.e()
        leng += 1
    while r.cs() is True:
        r.s()
        wid += 1
    x = leng * wid
    r.say(x)


def diamond():
    r = robot.Robot(4)
    x = 0
    leng = 1
    nums = list()
    while r.cs() is True:
        r.s()
        leng += 1
    nums.append(leng)
    while leng > 1:
        leng -= 2
        nums.append(leng * 2)
    x = sum(nums)
    r.say(x)


def diamond2():
    r = robot.Robot(5)
    while r.cn() is True:
        r.n()
    while r.ce() is True:
        r.e()
        if r.cn() is True:
            r.n()
    while r.cw() is True:
        r.w()
        if r.cn() is True:
            r.n()
    x = 0
    leng = 1
    nums = list()
    while r.cs() is True:
        r.s()
        leng += 1
    nums.append(leng)
    while leng > 1:
        leng -= 2
        nums.append(leng * 2)
    x = sum(nums)
    r.say(x)


def spiral1():
    r = robot.Robot(6)
    x = 0
    track = {'n': 0
        , 'e': 0
        , 's': 0
        , 'w': 0}
    while (r.cn() and r.ce() and r.cs()) or \
            (r.cn() and r.cs() and r.cw()) or \
            (r.cn() and r.ce() and r.cw()) or \
            (r.ce() and r.cs() and r.cw()) is False:
        if r.cn():
            while r.cn():
                r.n()
                track['n'] += 1
            while r.cw():
                r.w()
                track['w'] += 1
            while r.cs():
                r.s()
                track['s'] += 1
            while r.ce():
                r.e()
                track['e'] += 1
            if (r.cn() and r.ce() and r.cs()) is True:
                break
        elif r.cw():
            while r.cw():
                r.w()
                track['w'] += 1
            while r.cs():
                r.s()
                track['s'] += 1
            while r.ce():
                r.e()
                track['e'] += 1
            while r.cn():
                r.n()
                track['n'] += 1
            if (r.cn() and r.cs() and r.cw()) is True:
                break
        elif r.cs():
            while r.cs():
                r.s()
                track['s'] += 1
            while r.ce():
                r.e()
                track['e'] += 1
            while r.cn():
                r.n()
                track['n'] += 1
            while r.cw():
                r.w()
                track['w'] += 1
            if (r.cn() and r.ce() and r.cw()) is True:
                break
        elif r.ce():
            while r.ce():
                r.e()
                track['e'] += 1
            while r.cn():
                r.n()
                track['n'] += 1
            while r.cw():
                r.w()
                track['w'] += 1
            while r.cs():
                r.s()
                track['s'] += 1
            if (r.ce() and r.cs() and r.cw()) is True:
                break
    x = sum(track.values())
    r.say(x)

def sprial2():
    r = robot.Robot(7)

