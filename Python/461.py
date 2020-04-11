# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 461 - Almost Pi

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import numpy as np
from tqdm import tqdm, trange

progressbar = False


def F(n, k):
    return np.exp(k / n) - 1


def bisect(f, a, c):
    # discrete bisection method on monotonically increasing function to find zero.
    f_a, f_c = f(a), f(c)

    while c - a > 1:
        b = (c + a) // 2
        f_b = f(b)
        if f_b < 0:
            a = b
            f_a = f_b
        elif f_b > 0:
            c = b
            f_c = f_b

    if abs(f_a) < abs(f_c):
        return a
    elif abs(f_c) < abs(f_a):
        return c


def get_opt_k(n):
    # find the maximum value of k
    k_max = int(np.floor(n * np.log(1 + np.pi)))

    # pregenerate all values of F(n, k) that will be used.
    Fs = np.array([F(n, x) for x in range(k_max)])

    # Generate all sums of pairs of f(k) and sort the list.
    total = []
    fn = []
    eps = 0.01

    for a in trange(k_max):
        for b in range(a, k_max):
            this_F = Fs[a] + Fs[b]
            fn.append(this_F)
            total.append(a ** 2 + b ** 2)
            if this_F > np.pi + eps:
                break

    sort_ind = np.argsort(fn)
    fn = np.array(fn)[sort_ind]
    total = np.array(total)[sort_ind]

    N = len(fn)

    # use bisection to find pair of f(k1) + f(k2) which is closest to pi.
    cost_best = 9999
    k_best = -1

    for i in trange(N):
        e_func = lambda j: fn[i] + fn[j] - np.pi
        e_argmin = bisect(e_func, 0, N - 1)
        e_min = abs(e_func(e_argmin))

        if e_min < cost_best:
            cost_best = e_min
            k_best = total[i] + total[e_argmin]
    return k_best


def run():
    return get_opt_k(10000)


if __name__ == "__main__":

    print(run())
