# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
'''
let X = X1 + X2 + ... + X7, where Xi is 1 if colour i is present, and 0 if it
is not. Find E(X)
E(X) = E(X1 + X2 + ... + X7)
By applying linearity, it can be seen that:
E(X) = E(X1) + E(X2) + ... + E(X7)
By symmetry of each color,
E(X) = 7*E(Xi)
Consider the probability that a colour is not present:
E(X) = 7*(1 - ~E(Xi))
E(X) = 7*(1 - 60 choose 20/70 choose 20)
'''


from math import factorial

def nCk(n, k):
    return factorial(n)//(factorial(k)*factorial(n - k))


def run():
    ans = 7*(1 - nCk(60, 20)/nCk(70, 20))
    return '{:2.9f}'.format(ans)



if __name__ == "__main__":
    print(run())

