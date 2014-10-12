import unittest
from stack import *

class StackTestCase(unittest.TestCase):
    """Tests for `stack.py`."""

    def test_constructor(self):
        """Tests that the constructor makes an object"""
        s = Stack()
        self.assertIsInstance(s, Stack)

    def test_push_peek(self):
        '''Tests that the push function can add an object and the peek function can see it'''
        s = Stack()
        s.push(1)
        self.assertTrue(s.peek()==1)

    def test_push_pop(self):
        '''Tests the push and pop functions work as expected'''
        s =  Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        list = []
        list.append(s.pop())
        list.append(s.pop())
        list.append(s.pop())
        self.assertTrue(list == [3,2,1])

if __name__ == '__main__':
    unittest.main()
