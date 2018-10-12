# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 21:47:50 2018

@author: J
"""



import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('{}() executed in {} seconds.'.format(method.__name__, te - ts))
        return result

    return timed



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

def repeatedDecimal2(b):
# Returns the length of the repeating decimal for 1/b
# Does this by performing long division until a remainder is repeated
# aiming to beat 0.3031272888183594 sec


# USE THIS https://en.wikipedia.org/wiki/Multiplicative_order

    #note. doesnt work for numbers with prime divisors of 2 and/or 5. exclued these somehow
    a = 10
    order = 1
    while a%b != 1:
        a, order = a*10, order+1
    return order


@timeit
def run():
    sumL = 0
    for x in range(3, int(1e4)):
        if x%5==0:
            continue
        if x%2==0:
            continue
        sumL += repeatedDecimal2(x)

    return sumL



if __name__ == "__main__":
	print(run())