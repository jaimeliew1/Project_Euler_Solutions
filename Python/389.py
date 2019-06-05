# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 389 - Platonic Dice

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

An unbiased single 4-sided die is thrown and its value, T, is noted.
T unbiased 6-sided dice are thrown and their scores are added together. The sum, C, is noted.
C unbiased 8-sided dice are thrown and their scores are added together. The sum, O, is noted.
O unbiased 12-sided dice are thrown and their scores are added together. The sum, D, is noted.
D unbiased 20-sided dice are thrown and their scores are added together. The sum, I, is noted.
Find the variance of I, and give your answer rounded to 4 decimal places.


Used probability generating functions, and find a recursive solution
analytically.

let G_n(s) be the generating function for a dice of n sides.

G_n(s) = 1/n*(s + s^1 + s^2 + ... s^n)

By differentiating with respect to s, the mean, mu_n = G_n'(1) = (n+1)/2

an intermediate variable, G_n''(1)/mu_n = 2/3*(n-1)

The generating function of a dice being rolled t times, where t is the sum of
rolls of another dice is THE COMPOSITION of the individual generating functions.
Let H_i be the composed generating function of the first i dice.

so H_5 = G_4(G_6(G_8(G_12(G_20))))

let mu_i be the mean corresponding to H_i, and lambda_i be an intermediate
variable.

Find mu_5 and lambda_5 using the recursive relation:
mu_i = (n+1)/2*mu_(i-1)
lambda_i = 2/3*(n-1) + (n+1)/2*lambda_(i-1)
(note the use of the intermediate variable)

Then finally, the variance, var(H_5) is:

var(H_5) = mu_5*(lambda_i + 1 - mu_5)

It turns out the intermediate variable can be completely omitted by using Wald's
equation, or more algebra.

"""


def run():
    Lambda, Mu = 0, 1
    for n in [4, 6, 8, 12, 20]:
        Lambda = 2/3*(n-1) + (n+1)/2*Lambda
        Mu *= (n+1)/2

    variance = Mu*(Lambda + 1 - Mu)

    return f'{variance:2.4f}'


if __name__ == "__main__":
    print(run())
