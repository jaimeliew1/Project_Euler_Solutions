# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def TriNums(N):
    # returns the first N triangular numbers.
    trinums = []
    for i in range(1, N + 1):
        trinums.append(i*(i + 1)//2)
    return trinums

def wordValue(word):
    # returns the sum of the letter number position. assumes word is uppercase.
    return sum(ord(x)-64 for x in word)

def run():
    with open('Data/p042_words.txt') as f:
        words = f.read()[1:-1].split('","')

    trinums = TriNums(20)
    return sum(wordValue(word) in trinums for word in words)


if __name__ == "__main__":

    print(run())

