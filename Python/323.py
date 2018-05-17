# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
'''
probability of a single bit being zero after i rounds: 0.5**i
probability of a single bit being 1 after i rounds: 1 - 0.5**i
probability of 32 bits being 1 after i rounds: (1 - 0.5**i)**32
therefore CDF is P(rounds <= i) = (1 - 0.5**i)**32

E(rounds) = sum from i=0 to infinity of 1 - (1 - 0.5**i)**32
'''
def run():

    p = 0
    for i in range(0, 50):
        p += 1-(1-0.5**i)**32
        #print(i, '{:2.10f}'.format(p))
    return '{:2.10f}'.format(p)


if __name__ == "__main__":



    print(run())

