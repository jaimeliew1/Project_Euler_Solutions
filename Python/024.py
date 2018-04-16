# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 24

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import itertools




def run():
    lex = (0,1,2,3,4,5,6,7,8,9)
    a = list(itertools.permutations(lex))
    answer = ''
    for digit in a[999999]:
        answer += str(digit)

    return int(answer)


if __name__ == "__main__":
	print(run())

