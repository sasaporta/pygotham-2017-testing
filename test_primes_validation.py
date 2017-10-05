"""
Defines unit tests for the "primes" module.
"""

import pytest

from primes import is_prime


def test_is_prime_validation():

    # Checking for an exception long way...
    try:
        is_prime('a')
        assert False, 'should not have reached here'
    except RuntimeError as exc:
        assert str(exc) == 'not an integer'

    # ...And the short way.
    with pytest.raises(RuntimeError) as exc:
        is_prime('a')
    assert str(exc.value) == 'not an integer'
