"""
Performs calculations related to prime numbers.
"""

import math


def _verify_integer_greater_than_one(n):
    """
    Raises an exception if its argument is not an integer greater than one.
    """
    if not isinstance(n, int):
        raise RuntimeError('not an integer')
    if n < 2:
        raise RuntimeError('not greater than 1')


def is_prime(n):
    """
    Given an integer greater than 1, returns True if the integer is prime, false otherwise.
    """

    _verify_integer_greater_than_one(n)
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    max = int(math.sqrt(n))
    i = 3
    while True:
        if n % i == 0:
            return False
        i += 2
        if i > max:
            return True


def prime_factors(n):
    """
    Given an integer greater than 1, returns a sorted list of the integer's prime factors. Does not accept inputs
    greater than 1,000,000.
    """

    _verify_integer_greater_than_one(n)
    if n > 1000000:
        raise RuntimeError('greater than 1,000,000')
    primes = [p for p in range(2, 1000) if is_prime(p)]
    factors = []
    while n > 1:
        for p in primes:
            if n % p == 0:
                factors.append(p)
                n /= p
                if n == 1:
                    return factors
                break
