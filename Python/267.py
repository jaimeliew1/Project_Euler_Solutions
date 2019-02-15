import numpy as np
from scipy.optimize import minimize_scalar

def run():
    N = 1000

    # calculate binomial coefficients
    pascal = np.ones(N+1)
    for k in range(N):
        pascal[k+1] = pascal[k] * (N-k) / (k+1)

    # maximise probability of earning over 1e9
    cost = lambda f: -expected_profit(f, N, pascal)
    f_opt = minimize_scalar(cost, bracket=[0.1, 0.4]).x

    return '{:2.12f}'.format(expected_profit(f_opt, N, pascal))


def expected_profit(f, N, pascal):
    u, d = 1 + 2*f, 1-f # up profit, down loss

    R = np.zeros(N+1)
    R[0] = u**N
    for i in range(N):
        R[i+1] = R[i]*d/u

    return sum(pascal[R>=1e9])/sum(pascal)


if __name__ == '__main__':
    print(run())
