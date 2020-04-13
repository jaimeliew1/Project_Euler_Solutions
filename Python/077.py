# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 77 - Prime partitions

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import primelist

memo = {}


def ways(target, i_max, coins):
    if (target, i_max) in memo.keys():
        return memo[(target, i_max)]
    else:
        ans = _ways(target, i_max, coins)
        memo[(target, i_max)] = ans
        return ans


def _ways(target, i_max, coins):
    """
    Finds the number of ways of making 'target' from the sum of 'coins'
    """
    if target == 0:
        return 1
    if i_max == 0:
        if target % coins[0] == 0:
            return 1
        else:
            return 0
    elif coins[i_max] > target:
        return ways(target, i_max - 1, coins)
    elif coins[i_max] <= target:
        count = 0
        for n in range(target // coins[i_max] + 1):
            count += ways(target - n * coins[i_max], i_max - 1, coins)
        return count
    else:
        breakpoint()


def run():
    primes = primelist(100)
    for n in range(2, 100):
        num_ways = ways(n, len(primes) - 1, primes)
        if num_ways > 5000:
            return n


if __name__ == "__main__":
    print(run())
