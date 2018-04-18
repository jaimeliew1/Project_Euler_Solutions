# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def isPandigital(n):
    st = str(n)
    return all(st.count(str(x)) == 1 for x in range(1, 10))



def concatProduct(a, b):
    out = ''
    for i in range(1, b + 1):
        out += str(a*i)
    return out



def run():
    pandigitList = []
    for b in range(2, 10):
        a = pow(10, 9//b - 1)
        c = concatProduct(a, b)

        while len(c) < 10:
            if len(c) == 9:
                if isPandigital(c):
                    pandigitList.append(int(c))
            a += 1
            c = concatProduct(a,b)
    return max(pandigitList)


if __name__ == "__main__":
    print(run())

