import math
import functools
from collections import Counter
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print("Time elapsed for {}: {:2.4f}s".format(method.__name__, (te - ts)))
        return result

    return timed


# numDigits used in problems: ..., 25, 32
def numDigits(n):
    return math.floor(math.log10(n)) + 1


def primes_sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    for i in trange(2, int(N ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
    return is_prime


def primes_gen(n):
    # Generates prime numbers p < n
    a = [True] * (n + 1)
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, len(a), i):  # Mark factors non-prime
                a[n] = False


def primeFactors(x, primes, aslist=False):
    primefactors = Counter()
    while x > 1:
        for p in primes:
            if x % p == 0:
                x = x // p
                primefactors[p] += 1
                break
    if aslist:
        return list(primefactors.elements())
    else:
        return dict(primefactors)


def factors(x):
    factors = list([i, x // i] for i in range(1, int(pow(x, 0.5) + 1)) if x % i == 0)
    return set(functools.reduce(list.__add__, factors))


def primelist(n):
    # Returns list of prime numbers below n.
    return [i for i, p in enumerate(primes_sieve(n)) if p]


def multiplicative_partitions(n, min_divisor=2):
    # https://stackoverflow.com/questions/24723721/how-can-i-generate-all-possible-divisor-products-for-a-number
    """Generate expressions of n as a product of ints >= min_divisor."""
    if n == 1:
        yield []
    for divisor in range(min_divisor, n + 1):
        if n % divisor == 0:
            for product in multiplicative_partitions(n // divisor, divisor):
                yield product + [divisor]


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    # Miller–Rabin primality test
    if n == 1:
        return False
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(
        _try_composite(a, d, n, s) for a in _known_primes[:_precision_for_huge_n]
    )


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
