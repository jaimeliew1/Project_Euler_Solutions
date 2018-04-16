# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 31

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
coins = (200, 100, 50, 20, 10, 5, 2)
def numPennies(comb):
    Sum = 0
    for i, c in enumerate(coins):
        Sum += c*comb[i]
    return 200 - Sum


def run():

    count = 0
    currentComb = [0,0,0,0,0,0,0]
    while currentComb[0] != 1:
        if numPennies(currentComb) >= 0:
            count += 1
            currentComb[6] += 1

        else:
            for i in range(6,-1,-1):
                if numPennies(currentComb) < 0:
                    currentComb[i] = 0
                    currentComb[i-1] += 1

    count += 1 #The final combination is skipped in the previous loop

    return count

if __name__ == "__main__":
	print(run())

