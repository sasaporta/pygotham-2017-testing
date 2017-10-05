"""
Performs calculations related to prime numbers. Requires an authenticated user.
"""

import math


class User:
    """
    Represents a user, who has a username and a password.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password


def _validate_user(user):
    """
    Raises an exception if the username and password don't represent a valid user.
    """
    if user.username == 'python' and user.password == 'rocks':
        return
    raise RuntimeError('invalid user')


def _verify_integer_greater_than_one(n):
    """
    Raises an exception if its argument is not an integer greater than one.
    """
    if not isinstance(n, int):
        raise RuntimeError('not an integer')
    if n < 2:
        raise RuntimeError('not greater than 1')


def is_prime(user, n):
    """
    Given an integer greater than 1, returns True if the integer is prime, false otherwise.
    """

    _validate_user(user)
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


def prime_factors(user, n):
    """
    Given an integer greater than 1, returns a sorted list of the integer's prime factors. Does not accept inputs
    greater than 1,000,000.
    """

    _validate_user(user)
    _verify_integer_greater_than_one(n)
    if n > 1000000:
        raise RuntimeError('greater than 1,000,000')
    primes = [p for p in range(2, 1000) if is_prime(user, p)]
    factors = []
    while n > 1:
        for p in primes:
            if n % p == 0:
                factors.append(p)
                n /= p
                if n == 1:
                    return factors
                break
