#dld9jfn Daniel Disano aa3se Alisha Agrawal
import random


def ellipsis(s):
    new = s[0:2]+'..'+s[len(s)-2:len(s)]
    return new


def eighteen(s):
    length = len(s)-2
    new = s[0:1] + str(length) + s[len(s) - 1:len(s)]
    return new


def allit(s,t):
    s = s.lower()
    t = t.lower()
    si = s[0]
    ti = t[0]
    if 'a'in s[0] or 'e'in s[0] or'i'in s[0] or 'o'in s[0] or 'u'in s[0] or 'a'in t[0] or 'e'in t[0] or'i'in t[0] or'o'in t[0] or'u'in t[0]:
        return False
    elif si in ti:
        return True
    else:
        return False


def between(s,t):
    length = len(t)-1
    dex1 = s.find(t)
    dex2 = s.find(t,dex1 + 1,len(s))
    if dex2 < 0:
        return ""
    final1 = int(dex1+1+length)
    final2 = int(dex2)
    return s[final1:final2]


def rbetween(s,t):
    length = len(t)-1
    dex1 = s.rfind(t)
    dex2 = s.rfind(t,0,dex1)
    if dex2 < 0:
        return ""
    final1 = int(dex2+1+length)
    final2 = int(dex1)
    return s[final1:final2]


def rand_between(s,t):
    rand = random.randint(1,2)
    if rand == 1:
        return rbetween(s,t)
    elif rand == 2:
        return between(s,t)
