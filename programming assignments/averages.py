# Alisha Agrawal (aa3se)
"""
These functions return different
types of averages (mean, median,
root mean square, and the median
between those three averages
"""


# returns mean of three #s
def mean(a, b, c):
    comp_mean = (a + b + c) / 3
    return comp_mean


# returns median of three #s
def median(d, e, f):
    if (e >= d >= f) or (e <= d <= f):
        return d
    elif (f <= e <= d) or (d <= e <= f):
        return e
    else:
        return f


# returns root mean square
def rms(a, b, c):
    a = a**2
    b = b**2
    c = c**2
    comp_rms = mean(a, b, c) ** 0.5
    return comp_rms


# returns median b/n three types of averages
def middle_average(a, b, c):
    mean1 = mean(a, b, c)
    median1 = median(a, b, c)
    rms1 = rms(a, b, c)
    comp_ma = median(mean1, median1, rms1)
    return comp_ma
