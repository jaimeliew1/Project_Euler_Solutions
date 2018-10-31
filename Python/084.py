# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 84

Monopoly

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from collections import Counter
import random

N_sides = 4 # number of sides on die

railways = [5, 15, 25, 35]
utilities = [12, 28]
chances = [7, 22, 36]
community_chests = [2, 17, 33]

def get_community_chest(current_pos):
    rand = random.randint(1, 16)
    if rand == 1:
        return 0 # go to go
    elif rand == 2:
        return 10 # go to jail
    else:
        return current_pos

def get_chance(current_pos):
    chancemap = [0, 10, 11, 24, 39, 5]
    rand = random.randint(1, 16)
    if rand <= 6: # go to [location]
        return chancemap[rand-1]
    elif rand in [7, 8]: # go to next railway
        for rw in railways:
            if rw > current_pos:
                return rw
        else:
            return railways[0]
    elif rand == 9: # go to next utility
        for ut in utilities:
            if ut > current_pos:
                return ut
        else:
            return utilities[0]
    elif rand == 10: # go back 3 squares
        return (current_pos - 3)%40

    else:
        return current_pos



def get_move(current_pos, n_doubles):
    roll = random.randint(1, N_sides), random.randint(1, N_sides)
    if roll[0] == roll[1]:
        n_doubles += 1
    else:
        n_doubles = 0

    # if three doubles are rolled...
    if n_doubles == 3:
        n_doubles = 0
        return 10, n_doubles # go to jail

    next_pos = (current_pos + sum(roll)) % 40
    if next_pos in chances:
        next_pos = get_chance(next_pos)
    if next_pos in community_chests:
        next_pos = get_community_chest(next_pos)
    if next_pos == 30:
        next_pos = 10

    if next_pos == 10:
        n_doubles = 0
    return next_pos, n_doubles


def run():
    moveCount = Counter({x:0 for x in range(40)})
    current_pos = 0
    n_doubles = 0

    for i in range(1000000):
        moveCount[current_pos] += 1
        current_pos, n_doubles = get_move(current_pos, n_doubles)

    for loc, freq in moveCount.most_common(3):
        print('{}: {:2.2f}%'.format(loc, freq/sum(moveCount.values())*100))
    return ''.join('{:02d}'.format(x) for x, y in moveCount.most_common(3))

if __name__ == "__main__":
    print(run())




