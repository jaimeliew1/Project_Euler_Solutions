# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 173 - Using up to one million tiles how many
different "hollow" square laminae can be formed?

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Loop over all inner square side lengths between 1 and inner_max.

we know inner_max is 1e6//4 - 1.

then loop over all outer square side lengths until outer **2 - inner**2 > 1e6.
"""
from icecream import ic
from tqdm import trange


def run(tiles_max=1000000):
    count = 0
    inner_max = tiles_max // 4 - 1
    for inner in trange(1, inner_max + 1):
        outer = inner + 2
        while outer ** 2 - inner ** 2 <= tiles_max:
            count += 1
            outer += 2
        if outer == inner + 2:
            break

    return count


if __name__ == "__main__":
    print(run())
