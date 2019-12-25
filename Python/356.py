# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 356 - Largest roots of cubic polynomials

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Consider a cubic of the form: ax^3 + bx^2 + cx + d
with roots, r1, r2, and r3 where r1 >= r2 >= r3.

A large power of the largest root of the cubics approaches the SUM of the
powers of all three roots. That is,

r1^e -> r1^e + r2^e + r3^e.

Using Newtons Identities, the power sum of the roots of a cubic can be found
with a recursive relationship:

Let Pi = r1^i + r2^i + r3^i
then Pi = -b/a*P(i-1) -c/a*P(i-2) -d/a*P(i-3)
where P(0) = 3
P(1) = -b/a
P(2) = -b/a*P1 - 2*c/a
for this particular problem, the cubic is of the form:

x^3 - 2^n*x^2 + n       for n = 1 to 30

Therefore,
Pi = 2^n*P(i-1) - n*P(i-3)
where P(0) = 3,
P(1) = 2^n
P(2) = 2^(2n)

In matrix form, the recursive relation is shown as:

|2^n  0  -n|^(987654321-2)|2^(2n)|
|1    0   0|              |2^3   |
|0    1   0|              |3     |

The exponentiation is done using a binary exponentiation algorithm for speed,
where each matrix multiplication operation is performed modulo 10^8
"""

def modulo_matrix_exponentiate(A, exp, m):
    '''
    Performs large exponentiation of matrix A to the power of exp, where
    each operation is modulo m. Uses a binary, recursive exponentiation
    algorithm.

    '''
    if exp == 1:
        return A
    elif exp % 2 == 0:
        A_ = modulo_matrix_exponentiate(A, exp // 2, m)
        return modulo_matrix_multiply(A_, A_, m)
    elif exp % 2 == 1:
        A_ = modulo_matrix_exponentiate(A, exp - 1, m)
        return modulo_matrix_multiply(A_, A, m)


def modulo_matrix_multiply(A, B, m):
    '''
    Calculates (A@B)mod m, where A and B are 3x3 matrices.
    '''
    n = 3
    out = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(n):
        for j in range(n):
            out[i][j] = sum(A[i][k] * B[k][j] % m for k in range(n))
    return out


def run():
    m = 100000000
    exp = 987654321
    ans = {}

    for n in range(1, 31):
        A = [[2**n, 0, -n], [1, 0, 0], [0, 1, 0]]
        b = [2**(2 * n), 2**n, 3]
        a_exp = modulo_matrix_exponentiate(A, exp - 2, m)
        ans[n] = (b[0] * a_exp[0][0] +
                b[1] * a_exp[0][1] +
                b[2] * a_exp[0][2] - 1) % m


    return sum(ans.values()) % m


if __name__ == "__main__":
    print(run())
