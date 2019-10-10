from collections import Counter
from EulerFunctions import timeit


def isPalindrome(n):
    st = str(n)
    return st[::-1] == st


@timeit
def run():
    count = Counter()
    for i in range(100000):
        for j in range(1000):
            n = i**2 + j**3
            if isPalindrome(n):
                count[n] += 1

    return sum(key for key, val in count.items() if val==4)


if __name__ == '__main__':
    print(run())
