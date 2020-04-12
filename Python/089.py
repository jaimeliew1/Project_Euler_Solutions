# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 89 - Roman numerals

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():

    romNums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    data = []
    origNumChars = 0
    with open("Data/p089_roman.txt") as f:
        for line in f:
            data.append(line.strip())
            origNumChars += len(data[-1])

    numChars = 0
    for d in data:
        d = d.replace("VIIII", "IX")
        d = d.replace("IIII", "IV")
        d = d.replace("LXXXX", "XC")
        d = d.replace("XXXX", "XL")
        d = d.replace("DCCCC", "CM")
        d = d.replace("CCCC", "CD")
        numChars += len(d)

    return origNumChars - numChars


if __name__ == "__main__":
    print(run())
