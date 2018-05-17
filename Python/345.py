# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 345

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import numpy as np
from itertools import permutations, product
from math import factorial

_data_example = '''7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303'''

_data = '''7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805'''


'''
lemma 1:
    a vector of n elements can be arranged in n! different configurations.
    There are p(n) n!*n! possible matrix sums.
    p(5) = 14400 = '1.44e+04'
    p(15) = 1710012252724199424000000 =~ 1.71e+24
    Must find a better method than testing all combinations

try Hungarian algorithm https://en.wikipedia.org/wiki/Hungarian_algorithm

'''
def loadData(example=False):
    if example:
        _x = _data_example
    else:
        _x = _data
    x = []
    for line in _x.split('\n'):
        x.append([int(y) for y in line.split()])

    return np.array(x)



def naive(mat):
    N = len(mat)

    if N > 5:
        print('matrix too big')
        return 0

    perms = list(permutations(range(N), N))
    maxSum = 0
    for X, Y in product(perms, perms):
        Sum = sum(mat[x, y] for (x, y) in zip(X, Y))
        if Sum > maxSum:
            maxSum = Sum

    return maxSum


def run():
    return -1


if __name__ == "__main__":
    _mat = loadData(example=False)
    N = len(_mat)
    print(naive(_mat))

    mat = np.array(_mat)

    # refer to https://www.wikihow.com/Use-the-Hungarian-Algorithm

    # 1. for each row, subtract the minimum of that row.
    for i, row in enumerate(mat):
        mat[i, :] -= min(row)
    #print(mat)

    # 2. for each column without a zero, subtract the minimum of that column
    # from that column.
    for i in range(N):
        if 0 not in mat[:, i]:
            mat[:, i] -= min(mat[:, i])
    print(mat)

    # 3. Draw a line through each column and row which has a zero. Find the
    # minimum number of lines which covers all zeros. note: draw lines through
    # columns/rows with most zeros first.

    # 4.Add the minimum uncovered element to every covered element. If an
    # element is covered twice, add the minimum element to it twice.

    # 5. Subtract the minimum element from every element in the matrix.

    # repeat steps 3 to 5 until the minimum number of lines = N.

    #print(run())

