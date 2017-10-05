import pytest


@pytest.fixture()
def func_in_conftest():
    print 'This function is in conftest.py'
