import unittest
from parens import is_closed

class ParensTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_balanced(self):
        """Does the function return 0 on a properly matched set of parentheses?"""
        self.assertTrue(is_closed('(())') == 0)

    def test_open(self):
        '''Does the function return 1 when there are too many opening parentheses?'''
        self.assertTrue(is_closed('((())') == 1)

    def test_broken(self):
        '''Does the function return -1 when there are too many closing parentheses?'''
        self.assertTrue(is_closed('(()))') == -1)

    def test_wrong_order(self):
        '''Does the function return -1 when  there are the right number of parens in an invalid order?'''
        self.assertTrue(is_closed(')(') == -1)

if __name__ == '__main__':
    unittest.main()
