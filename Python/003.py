# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 3

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import primelist

def run():
    N = 600851475143

    return max(p for p in primelist(int(N**0.5)) if N%p == 0)



if __name__ == "__main__":
	print(run())
