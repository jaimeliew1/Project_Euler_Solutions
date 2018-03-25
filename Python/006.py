# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 6

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def run():
    N = 100
    return sum(i for i in range(N+1))**2 - sum(i**2 for i in range(N+1))



if __name__ == "__main__":
    print(run())
