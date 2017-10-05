"""
Illustrates running tests in parallel.
"""

import sys
import time


def test_parallel_one():
    for i in range(5):
        print >>sys.stderr, 'Test 1:', i
        time.sleep(1)


def test_parallel_two():
    for i in range(5):
        print >>sys.stderr, 'Test 2:', i
        time.sleep(1)


def test_parallel_bad_1():
    user = create_test_user('mary')
    test_something(user=user)
    delete_all_test_users()


def test_parallel_bad_2():
    user = create_test_user('bob')
    test_something_else(user=user)
    delete_all_test_users()
