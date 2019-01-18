# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 93

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from operator import add, truediv, mul, sub
from itertools import product, permutations, combinations

Operations = {  '+': add,
                '-': sub,
                '*': mul,
                '/': truediv,
                '/r': lambda a, b: b/a, # reverse division
                '-r': lambda a, b: b-a} # reverse subtraction

def run():
    best_digit_set, best_length = [0, 0, 0, 0], 0
    for digit_set in combinations(range(1, 10), 4):
        outcomes = set()
        for a, b, c, d in permutations(digit_set):
            for op1, op2, op3 in product(Operations.values(), repeat=3):
                try:
                    outcomes.add(op1(a, op2(b, op3(c, d)))) # (((a . b) . c) . d)
                except ZeroDivisionError: pass
                try:
                    outcomes.add(op1(op2(a, b), op3(c, d))) # ((a . b) . (c . d))
                except ZeroDivisionError: pass
        outcomes = [int(x) for x in outcomes if float(x).is_integer() and x>0]
        outcomes = sorted(outcomes)

        streak = 0
        for i, val in enumerate(outcomes):
            if val == i+1:
                streak += 1
            else:
                break

        if streak > best_length:
            best_digit_set, best_length = digit_set, streak

    return(''.join([str(x) for x in best_digit_set]))




if __name__ == "__main__":
    print(run())
