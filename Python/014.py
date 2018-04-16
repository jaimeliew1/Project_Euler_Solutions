# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 12

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def CollatzSequence(n):
    # returns the collatz sequence in a list for starting number n.
    seq = [n]
    while n != 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        seq.append(n)
    return seq

def run():
    maxLength = 1
    startNum = None

    for i in range(1,1000000):
        length = len(CollatzSequence(i))
        if length > maxLength:
            maxLength, startNum = length, i

    return startNum

if __name__ == "__main__":

    print(run())
