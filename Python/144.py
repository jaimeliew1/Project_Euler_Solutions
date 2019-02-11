# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 144

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def run(plot=False):
    x, y = [0, 1.4], [10.1, -9.6]

    while not(abs(x[-1]) <= 0.01 and y[-1] > 0):
        v     = [x[-1] - x[-2], y[-1] - y[-2]] #current beam vector
        slope = -4*x[-1]/y[-1] # slope of ellipse at point of contact
        m     = reflect(slope, v) # slope of reflected beam

        # function for reflected beam
        line = lambda XX: y[-1] + (XX - x[-1])*m
        # function to find intersection of line and ellipse via root finding.
        cost = lambda XX: 4*XX**2 + line(XX)**2 - 100

        # first approximation of next point of contact
        X     = np.linspace(-5, 5, 1000)
        X     = X[abs(X-x[-1]) > 0.1]
        i_min = np.argmin(abs(cost(X)))

        # refined approximation of next point of contact
        xmin = newton(cost, X[i_min])

        # save
        y.append(line(xmin))
        x.append(xmin)

    if plot:
        make_plot(x, y)

    return len(x) - 2



def reflect(m, v):
    # reflects a line, v, about a surface, m, and returns the slope of the
    # reflected line. This relationship was derived by hand. Do you remember
    # how to do it?
    A = np.array([[1-m**2, 2*m],
                  [2*m,    m**2-1]])/(m**2 + 1)
    ans = np.matmul(A,v)

    return ans[1]/ans[0]


def make_plot(x, y):
    theta = np.linspace(0, 2*np.pi, 10000)
    r     = 10/np.sqrt(3*np.sin(theta)**2 + 1)

    x_ellipse, y_ellipse = r*np.sin(theta), r*np.cos(theta)

    fig = plt.figure(figsize=[8,8])
    plt.axis('equal')
    plt.plot(x_ellipse, y_ellipse, 'k')

    plt.plot(x, y)
    plt.plot(x[-1], y[-1], 'xr')



    plt.show()

if __name__ == "__main__":
    print(run(plot=True))
