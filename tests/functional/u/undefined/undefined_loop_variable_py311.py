"""Tests for undefined-loop-variable using Python 3.11 syntax."""

from typing import Never


def for_else_never(iterable):
    """Test for-else with Never type."""

    def idontreturn() -> Never:
        """This function never returns."""

    while True:
        for thing in iterable:
            break
        else:
            idontreturn()
        print(thing)

def for_else_return(iterable):
    """Test for-else with return"""

    while True:
        for thing in iterable:
            break
        else:
            return
        print(thing)

def for_else_break(iterable):
    """Test for-else with breaking from the outer loop"""

    while True:
        for thing in iterable:
            break
        else:
            break
        print(thing)

def for_else_raise(iterable):
    """Test for-else with throwing an exception"""

    while True:
        for thing in iterable:
            break
        else:
            raise Exception
        print(thing)
