# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 22

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def run():
    with open('Data/names.txt') as f:
        names = [x[1:-1] for x in f.read().split(',')]
    names.sort()

    totalScore = 0
    for i, name in enumerate(names, 1):
        score = i*sum(ord(letter) - 64 for letter in name)

        totalScore += score

    return totalScore


if __name__ == "__main__":
	print(run())

