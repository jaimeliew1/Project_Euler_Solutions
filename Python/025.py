# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import numDigits


def Fibonacci():
    a, b = 0, 1
    yield b
    while True:
        a, b = b, a + b
        yield b



def run():
    for i, x in enumerate(Fibonacci()):
        if numDigits(x) == 1000:
            return i + 1



if __name__ == "__main__":
	print(run())

