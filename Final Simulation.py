# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 01:02:16 2024

@author: kvmal
"""

class rand_num_gen:
    def __init__(self, a = 24693, c = 3517, K = 2**17, seed=1000):
        self.a = a
        self.c = c
        self.K = K
        self.x_prev = seed

    def  generate(self):
        self.x_prev = (self.a*self.x_prev+self.c)%self.K
        return self.x_prev
    
K = 2**17
lcg = rand_num_gen()
test_u_vals = []
for i in range(53):
    test_u_vals.append(lcg.generate()/K)

def switchboard(w):
    n = 1
    while n <= 3:
        ui = lcg.generate()/K
        n = n + 1
        w = w + 3 # each time the caller redials, they add 3 secs to wait time
        if ui <= 0.125 * (1.5) ** (3/2):
            w = w + 5 + (240 * (ui) ** (2/3))
            return w, True #return ends the loop if the caller connects, passes info that caller connected
        else:
            w = w + 92
    return w, False #return ends the function if caller gives up, passes info that caller gave up

def disc_rvg (w):
    ui = lcg.generate()/K # placeholder name for the random number gen that khalid will write
    if ui <= 0.2:
        w = w + 1.2 * 60 # if assigned to agent A
    elif ui <= 0.5:
        w = w + 1.6 * 60 # if assigned to agent B
    elif ui <= 0.6:
        w = w + 1.35 * 60 # if assigned to agent C
    else:
        w = w + 1.9 * 60 # if assigned to agent D
    return w

wait_times = []

for i in range (500):
    w = 0
    w, connected = switchboard(w) # connected stores boolean for whether person was connected
    if connected:
        w = disc_rvg(w)
    wait_times.append(w)
    
wait_times.sort()