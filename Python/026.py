# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 26

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def repeatedDecimal(a, b):
# Returns a string of the repeating decimal for a/b
# Does this by performing long division until a remainder is repeated
    dividend = a
    remainderList = []
    repDec = ''

    #get first quotient
    while (dividend//b == 0):
        dividend *= 10

    currentRem = dividend - b*(dividend//b)
    dividend = currentRem*10

    while currentRem not in remainderList:
        remainderList.append(currentRem)
        repDec += str(dividend//b)
        currentRem = dividend - b*(dividend//b)
        dividend = currentRem*10

    if 0 in remainderList:
        return ''
    else:
        return repDec




def run():
    xMax, Lmax = 0, 0
    for x in range(1, 1000):
        repDec = repeatedDecimal(1, x)
        if len(repDec) > Lmax:
            xMax, Lmax = x, len(repDec)

    return xMax



if __name__ == "__main__":
	print(run())

