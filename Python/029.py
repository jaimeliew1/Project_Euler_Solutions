# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():

    terms = set()
    limit = 100
    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            terms.add(a**b)

    return len(terms)


if __name__ == "__main__":
	print(run())

