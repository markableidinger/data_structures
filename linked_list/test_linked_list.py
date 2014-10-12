import unittest
from linked_list import *


class LinkedListTestCase(unittest.TestCase):
    """Tests for `linked_list.py`."""

    def test_constructor(self):
        """Tests that the constructor makes an object"""
        l = Linked_list()
        self.assertIsInstance(l, Linked_list)

    def test_insert(self):
        '''Tests that the insert function works'''
        l = Linked_list()
        l.insert(1)
        self.assertTrue(l.head.value == 1)

    def test_search(self):
        '''Tests that the search function works'''
        l = Linked_list()
        l.insert(1)
        l.insert(2)
        l.insert(3)
        self.assertTrue(l.search(2))

    def test_search_false(self):
        '''Tests to make sure search does not return false positives'''
        l = Linked_list()
        self.assertFalse(l.search(2))

    def test_remove(self):
        l = Linked_list()
        l.insert(1)
        l.insert(2)
        l.insert(3)
        l.remove(2)
        self.assertFalse(l.search(2))

    def test_pop(self):
        l = Linked_list()
        l.insert(1)
        l.insert(2)
        l.insert(3)
        f = []
        f.append(l.pop())
        f.append(l.pop())
        f.append(l.pop())
        self.assertTrue(f == [3, 2, 1])

    def test_size(self):
        l = Linked_list()
        l.insert(1)
        l.insert(2)
        l.insert(3)
        l.remove(1)
        l.pop()
        self.assertTrue(l.size() == 1)

if __name__ == '__main__':
    unittest.main()
