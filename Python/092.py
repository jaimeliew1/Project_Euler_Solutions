# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 92 - Square digit chains

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from tqdm import trange

def run():
    count = 0
    leadsTo89 = set([89])
    leadsTo1 = set([1])
    for n in trange(1, int(1e7)):
        checked = []

        while True:
            n = sum(int(x) ** 2 for x in str(n))
            checked.append(n)
            if n in leadsTo89:
                count += 1
                leadsTo89.update(checked)

                break
            if n in leadsTo1:
                leadsTo1.update(checked)
                break

    return count


if __name__ == "__main__":
    print(run())
