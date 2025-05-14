"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo


def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules


#h = montecarlo.BitString(10)
#h.set_integer_config(45)
#print(h.integer())
#print(h.config)

def testBitString():
    h = montecarlo.BitString(10)
    h.set_integer_config(45)

    assert(h.integer() == 45)

    h.flip_site(9)

    assert(h.integer() == 44)


if __name__ == "__main__":
    testBitString()
    test_montecarlo_imported()