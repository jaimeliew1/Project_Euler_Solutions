# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 346

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
'''
x = 1111_2 is a 4 digit number in base 2 consisting of only ones.
x = 2^0 + 2^1 + 2^2 + 2^3 = 15

y = 111...111_b is an n digit number in base b consisting of only ones.
y = b^0 + b^1 + ... + b^(n-1)

lemma 1:
    y is a repunit in base y-1 with length n=2. So ignore these and start search
    with n=3.

lemma 2:
    the base of repunit y is always less than y.

lemma 3:
    there are only two numbers which are repnumbers in 3 bases (or more): 31
    and ?. so use a set.

lemma 4:
    10e12^(1/2) = 1000000. This is the largest base that needs to b searched as
    we are only looking for repunits with length => 3. y_b,3 = 1 + b + b^2

'''



def run():
    limit = 1e12
    baselimit = int(limit**0.5)

    repunit = {1}

    for b in range(2, baselimit):
        n = 3
        y = (b**n - 1)//(b-1)
        while y < limit:
            repunit.add(y)
            n += 1
            y = (b**n - 1)//(b-1)

    return sum(repunit)


if __name__ == "__main__":

    print(run())

