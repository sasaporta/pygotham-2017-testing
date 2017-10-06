"""
Defines unit tests for the "primes" module, with authentication, using a fixture.
"""

import pytest

from primes_auth import is_prime, prime_factors, User


@pytest.fixture()
def user():
    print 'Creating user.'
    return User('python', 'rocks')


def test_is_prime(user):
    assert is_prime(user, 2) is True
    assert is_prime(user, 3) is True
    assert is_prime(user, 4) is False


def test_prime_factors(user):
    assert prime_factors(user, 2) == [2]
    assert prime_factors(user, 12) == [2, 2, 3]
