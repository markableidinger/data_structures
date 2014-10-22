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

    def test_empty(self):
        '''Tests if the function returns 0 on an empty string'''
        self.assertTrue(is_closed('') == 0)

    def test_single_open(self):
        '''Tests if the function returns 1 with 1 open parenthese'''
        self.assertTrue(is_closed('(') == 1)

    def test_single_closed(self):
        '''Tests if the function returns -1 with 1 closed parenthese'''
        self.assertTrue(is_closed(')') == -1)

    def test_single_pair(self):
        '''Tests if the function returns 0 with a single pair'''
        self.assertTrue(is_closed('()') == 0)

    def test_none(self):
        '''Tests if the function raises an exception if the input is None'''
        with self.assertRaises(TypeError):
            is_closed(None)


if __name__ == '__main__':
    unittest.main()
