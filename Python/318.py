# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 318 - 2011 nines

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

summary: (\sqrt{p} + \sqrt{q})^{2n} +(\sqrt{p} - \sqrt{q})^{2n} is an integer,
and \sqrt{p} - \sqrt{q} < 1 is a necessary condition.

According to Newton's Identities: the sum of the powers of roots of a polynomial
is an integer if the coefficients of that polynomial are integers. So all we
have to do is show that $\sqrt{p} + \sqrt{q}$ looks something like a root of a
polynomial with integer coefficients.

Let's start by defining $x = \sqrt{p} + \sqrt{q}$. Squaring both sides gives:
$x^2 = p + q + 2\sqrt{pq}$
$==> x^2 -p -q = 2\sqrt{pq}$

Squaring both sides again gives:
$(x^2 -p -q)^2 = 4pq$
$==> x^4 - 2(p+q)x^2 + (p-q)^2 = 0$

This is a fourth-order polynomial with integer coefficients. Therefore, the sum
of the powers of the roots must also be integers as mentioned before. The 4
roots of this polynomial are: $x_{root} = \pm\sqrt{p} \pm \sqrt{q}$

Great, so now we have a polynomial with integer coefficients, where one of the
roots is the quantity $\sqrt{p} + \sqrt{q}$ from the problem. Now let's consider
the sum of the powers of these roots. In fact, lets just consider the even
powers, as this is relevant to the problem: $(\sqrt{p} + \sqrt{q})^{2n} +
(\sqrt{p} - \sqrt{q})^{2n} + (\sqrt{q} - \sqrt{p})^{2n} + (-\sqrt{p} -
\sqrt{q})^{2n} = $ an integer

For integer $n$. As the exponent is even, we can see that the first and last
terms must be equal, and so are the middle two terms: $2(\sqrt{p} +
\sqrt{q})^{2n} + 2(\sqrt{p} - \sqrt{q})^{2n}  = $ an integer

Therefore, dividing everything by 2:
$(\sqrt{p} + \sqrt{q})^{2n} + (\sqrt{p} - \sqrt{q})^{2n}  = $ an integer

QED

Now, in order for the first term, $(\sqrt{p} + \sqrt{q})^{2n}$, to approach an
integer as $n --> \infty$, then the second term, $(\sqrt{p} -
\sqrt{q})^{2n}$ must approach zero as $n --> \infty$. This can only
happen when $\sqrt{p} - \sqrt{q} < 1$.

So now we just consider the term (\sqrt{p} - \sqrt{q})^(2n), which must have
2011 zeros after the decimal. This is found using logs to find exponent n.
"""
import numpy as np

def run():


    ans = 0
    for i in range(2, 2012):
        for p in range(1, i//2 + 1): # loop over all p and q where p+q < 2011, and p < q.
            q = i - p
            if p == q: continue
            if p + q - 2*np.sqrt(p*q) < 1:
                exp_min = int(-2011/np.log10(p + q - 2*np.sqrt(p*q))) + 1
                ans += exp_min

    return ans


if __name__ == "__main__":
    print(run())
