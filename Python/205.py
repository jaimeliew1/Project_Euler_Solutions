# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 205 - Dice Game

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import numpy as np


def dice_pdf(s, N):
    pdf_die = 1 / s * np.ones(s)
    pdf = pdf_die

    for i in range(N - 1):

        pdf = np.convolve(pdf, pdf_die)

    x = np.arange(N, N * s + 1)

    return x, pdf


def run():
    s1 = 4  # number of sides on die
    N1 = 9  # number of dice

    s2 = 6
    N2 = 6

    x1, pdf1 = dice_pdf(s1, N1)
    x2, pdf2 = dice_pdf(s2, N2)
    mean1 = sum(x1 * pdf1)
    mean2 = sum(x2 * pdf2)

    pdfGame = np.convolve(pdf1, pdf2)
    x3 = np.arange(1, len(pdfGame) + 1) - 28
    Pwin = sum(pdfGame[x3 > 0])

    return "{:2.7f}".format(Pwin)


if __name__ == "__main__":
    print(run())
