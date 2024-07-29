# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:50:06 2024

@author: kvmal
"""
import random


def disc_rvg(w):
    x = random.uniform(0,1) # placeholder name for the random number gen that khalid will write
    if x <= 0.2:
        w = w + 1.2 * 60 # if assigned to agent A
        a = 1
    elif x <= 0.5:
        w = w + 1.6 * 60 # if assigned to agent B
        a = 2
    elif x <= 0.6:
        w = w + 1.35 * 60 # if assigned to agent C
        a = 3
    else:
        w = w + 1.9 * 60 # if assigned to agent D
        a = 4
    return w, x, a
