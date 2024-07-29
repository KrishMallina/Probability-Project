from numpy import *
from cmath import *
from disc_rvg_test import *
from pandas import *
""" n => number of dials
    x => wait time until reaching switchboard, used in disc_rvg
    w => total wait time in sec
    u => random variable between 0 and 1 that determines
        the time it takes to reach the switchboard; the number of u values is equal to n
    a => variable between 0 and 4 that designates which
        agent was reached (0 = no agent reached, 1 = agent A, 2 = agent B, 3 = agent C, 4 = agent D)
"""
w_list = {}

for i in range(0, 500):
    n = 1
    w = 0
    u = 0
    end = False
    ticket = False
    agent = 'No agent reached'
    u_list = []

    #beginning of caller attempt
    while n <= 3 and not ticket:
        # dial
        w += 3
        u = random.uniform(0, 1)
        u = round(u, 4)
        u_list.append(u)
        if u <= 0.7704:
            # reaches switchboard
            w += 5 + 240 * u ** (2 / 3)
            # reaches agent
            w, u, a = disc_rvg(w)
            if a == 0:
                agent = 'No agent reached'
            elif a == 1:
                agent = 'Agent A'
            elif a == 2:
                agent = 'Agent B'
            elif a == 3:
                agent = 'Agent C'
            else:
                agent = 'Agent D'
            ticket = True

        else:
            # caller hangs up
            w += 2
            if n == 3:
                break
            n += 1
            ticket = False


    w = round(w, 4)
    u = round(u, 4)
    w_list[f'{i+1}'] = u_list, w, n, agent, ticket


df = DataFrame.from_dict(w_list, orient='index', columns=['u', 'w', 'n', 'agent', 'Ticket'])

print(df)
print(w_list['51'][0], w_list['52'][0], w_list['53'][0])