# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from string import ascii_letters

def run():
    with open('Data/p059_cipher.txt') as f:
        cipher = list(int(i) for i in f.read().split(','))

    key = [' ', ' ', ' ']
    # find each key letter individually by finding characters in ascii_letters
    for i in range(0,3):
        bestScore = 0
        for k in ascii_letters:
            score = 0
            for letter in cipher[i::3]:
                if 97 <= letter^ord(k) <= 122:
                    score += 1
            if score > bestScore:
                key[i] = k
                bestScore = score

    ans = ''
    for i, letter in enumerate(cipher):
        ans += chr(letter^ord(key[i%3]))


    #print(ans)
    return sum(ord(x) for x in ans)


if __name__ == "__main__":


    print(run())

