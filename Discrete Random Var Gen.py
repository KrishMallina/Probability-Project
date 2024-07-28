# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:50:06 2024

@author: kvmal
"""

def disc_rvg (w):
    x = rng() # placeholder name for the random number gen that khalid will write
    if x <= 0.2:
        w = w + 1.2 * 60 # if assigned to agent A
    elif x <= 0.5:
        w = w + 1.6 * 60 # if assigned to agent B
    elif x <= 0.6:
        w = w + 1.35 * 60 # if assigned to agent C
    else:
        w = w + 1.9 * 60 # if assigned to agent D
    return w