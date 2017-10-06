"""
Defines unit tests for the "primes" module.
"""

import pytest

from primes import is_prime, prime_factors


def test_is_prime():
    print 'This is test_is_prime'
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False


def test_prime_factors():
    print 'test_prime_factors'
    assert prime_factors(2) == [2]
    assert prime_factors(12) == [2, 2, 3]


@pytest.mark.parametrize('n', [2, 3, 5])
def test_parameterized_without_fixture(n):
    print 'n =', n
    assert is_prime(n)
