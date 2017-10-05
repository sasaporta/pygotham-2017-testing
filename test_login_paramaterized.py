"""
Illustrates parameterized fixtures by testing the "prime" module's authentication.
"""

import pytest

from primes_auth import is_prime, User


@pytest.fixture(params=[('rocks', True), ('bogus', False)])
def user(request):
    return User('python', request.param[0])


def test_auth(user):
    print 'user =', user.password
    try:
        is_prime(user, 2)
        print 'authenticated'
    except RuntimeError:
        print 'not authenticated'


def test_fixture_in_conftest(func_in_conftest):
    pass
