import math


def numDigits(n):
    return math.floor(math.log10(n))+1



def primes_sieve(n):
    # Returns boolean array indicating if each number is prime or not.
    # Sieve of Eratosthenes.
    a = [True] * (n+1)
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:

            for n in range(i*i, len(a), i):     # Mark factors non-prime
                a[n] = False
    return a

#def list_primality(n):
#	# Sieve of Eratosthenes
#	result = [True] * (n + 1)
#	result[0] = result[1] = False
#	for i in range(sqrt(n) + 1):
#		if result[i]:
#			for j in range(i * i, len(result), i):
#				result[j] = False
#	return result


def primelist(n):
    # Returns list of prime numbers below n.
    return [i for i, p in enumerate(primes_sieve(n)) if p]



def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):
    #Miller–Rabin primality test
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
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]