import unittest
from dll import *


class DLLTestCase(unittest.TestCase):
    '''Tests for dll.py'''

    def test_constructor(self):
        '''Tests that the constructor creates the correct object'''
        test_dll = Doubly_linked_list()
        self.assertIsInstance(test_dll, Doubly_linked_list)

    def test_insert(self):
        '''Tests that insert puts a value at the head'''
        test_dll = Doubly_linked_list()
        test_dll.insert(1)
        test_dll.insert(2)
        self.assertTrue(test_dll.head.next.value == 2)

    def test_append(self):
        '''Tests that append puts a value at the tail of the list'''
        test_dll = Doubly_linked_list()
        test_dll.append(1)
        test_dll.append(2)
        self.assertTrue(test_dll.tail.previous.value == 2)

    def test_pop(self):
        '''Tests that pop returns and removes appropriate value'''
        test_dll = Doubly_linked_list()
        test_dll.append(1)
        test_dll.append(2)
        return_list = []
        return_list.append(test_dll.pop())
        return_list.append(test_dll.pop())
        self.assertTrue(return_list == [1, 2])

    def test_shift(self):
        '''Tests that shift returns and removes appropriate value'''
        test_dll = Doubly_linked_list()
        test_dll.append(1)
        test_dll.append(2)
        return_list = []
        return_list.append(test_dll.shift())
        return_list.append(test_dll.shift())
        self.assertTrue(return_list == [2, 1])

    def test_pop_shift_remove_empty(self):
        '''Tests that shift, remove, and pop don't break it when the list is empty'''
        test_dll = Doubly_linked_list()
        test_dll.pop()
        test_dll.pop()
        test_dll.shift()
        test_dll.shift()
        test_dll.remove(1)
        test_dll.remove(2)
        test_dll.append(1)
        test_dll.append(2)
        return_list = []
        return_list.append(test_dll.pop())
        return_list.append(test_dll.shift())
        self.assertTrue(return_list == [1, 2])

    def test_remove(self):
        '''Tests that remove removes the correct value'''
        test_dll = Doubly_linked_list()
        test_dll.append(1)
        test_dll.append(2)
        test_dll.append(3)
        test_dll.remove(2)
        return_list = []
        return_list.append(test_dll.pop())
        return_list.append(test_dll.pop())
        return_list.append(test_dll.pop())
        self.assertTrue(return_list == [1, 3, None])
