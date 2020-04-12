# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 85 - Counting rectangles

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def numRects(w, h):
    return w * (w + 1) * h * (h + 1) // 4

def run():
    N = 2000000

    ans = [0, 0, 999999999]
    for i in range(1, 2001):
        for j in range(i, 2001):
            numrects = numRects(i, j)
            if abs(numrects - N) < ans[2]:
                ans = [i, j, abs(numrects - N), i * j]
                #print(ans)
            if numrects > N + ans[2]:
                break

    return ans[3]


if __name__ == "__main__":
    print (run())
