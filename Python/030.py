# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 30

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

# how was this limit chosen?
limit = 999999

def run():
    terms = []
    for i in range(2, limit):
        sumofFifths = sum(int(d)**5 for d in str(i))
        if sumofFifths == i:
            terms.append(i)

    #print(terms)
    return sum(terms)


if __name__ == "__main__":
	print(run())

