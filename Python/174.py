# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 174 - Counting the number of "hollow" square
laminae that can form one, two, three, ... distinct arrangements

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from collections import Counter
from tqdm import trange

def run(tiles_max=1000000):
    counter = Counter()
    inner_max = tiles_max // 4 - 1
    for inner in trange(1, inner_max + 1):
        outer = inner + 2
        tiles = outer ** 2 - inner ** 2
        while tiles <= tiles_max:
            counter[tiles] += 1
            outer += 2
            tiles = outer ** 2 - inner ** 2
        if outer == inner + 2:
            break

    return len([y for y in counter.values() if y<=10])



if __name__ == "__main__":
    print(run())
