from numpy import *
from cmath import *
from discrete_random_var_gen import *
from pandas import *
""" n => number of dials
    x => wait time until reaching switchboard
    w => total wait time in sec
    u => random variable between 0 and 0.2296
"""
i = 0
for i in range(0, 499):
    n = 0
    w = 0
    while n < 0:
        x = random.uniform(0, 0.2296)
        n += 1
        w += 3
        #Dial

        if x < 90:
            #to switchboard
            w += 5
            w += 240*u^(2/3)


        else:
            #hang-up
            w += 90 + 2
            #redial?
            if n = 3:
                print("The caller has called 3 times without getting a ticket.")
                break