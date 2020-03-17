import math, sys
from myutils import float_range


m, s, p1, p2 = 0, 1, -10, 10
for i, arg in enumerate(sys.argv[1:]):
    if i == 0: m = int(arg)
    elif i == 1: s = int(arg)
    elif i == 2: p1 = int(arg)
    elif i == 3: p2 = int(arg)

precision = 5

snd = lambda x : (math.e**((-x**2)/2*(1**2))) / (math.sqrt(2*math.pi))
nd = lambda x, m, s : (math.e**((-(x - m)**2)/2*(s**2))) / (s * math.sqrt(2*math.pi))

def integrate(func, a, b, precision = 5):
    return sum([ func(x) / 10**precision for x in float_range(precision, a, b) ])

print(round(integrate(nd, p1, p2), 4))

#print(round(sum([ (lambda x : (math.e**((-(x - m)**2)/2*(s**2))) / (s * math.sqrt(2*math.pi)))(x) / 10**precision for x in float_range(precision, p1, p2) ]), 4))

