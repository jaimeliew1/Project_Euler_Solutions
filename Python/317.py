# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 317

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Completed by hand. The path a projectile takes when launched from the origin is:
y = x*tan(t) -g*x^2/(2*v0^2)*sec^2(t)    (1)

for angle from horizontal of t, initial projectile velocity of v0
to get the envelope of the projectile motion, set dy/dt = 0, giving:

tan(t) = v0^2/(2*g)                    (2)
and with a bit of pythag, you can also get:
sec^2(t) = v^4/(g^2*x^2) + 1           (3)

substituting (2) and (3) into (1) gives the envelope, which also happens to be
a parabola:
y = v^2/(2g) - g*x^2/(2v^2)

or rearranging to give

x^2 = 2*v^2/(2g) * (v^2/(2*g) - y)

We can observe that the highest point (x=0) is y=v^2/(2g) as expected.
Now we can integrate to get the solid of revolution, V, by integrating
x^2 from y=-100 to y=2*v^2/(2g) multiplied by pi.

This gives V = 2*pi*v0**2/g*(v0**4/(8*g**2) + 100*v0**2/(2*g) + 100**2/2)
or         V = pi*v0**2/g*(v0**2/(2*g) + 100)**2
"""

from math import pi
def run():
    v0 = 20     # m/s
    g  = 9.81   # m/s^2
    V  = pi*v0**2/g*(v0**2/(2*g) + 100)**2
    return '{:2.4f}'.format(V)


if __name__ == "__main__":
    print(run())
