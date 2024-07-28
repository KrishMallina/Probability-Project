from numpy import *
from cmath import *
""" n => number of dials
    x => wait time until reaching switchboard
    w => total wait time in sec
    u => random variable between 0 and 0.2296
"""
n = 0
w = 0
while n < 0:
    x = 0
    n += 1
    w += 3
    #Dial
    x = 0.2296 * random()
    if x < 90:
        #to switchboard
        w += x

    else:
        #hang-up
        w += 90 + 2
        #redial?
        if n = 3:
            print("The caller has called 3 times without getting a ticket.")
            break

