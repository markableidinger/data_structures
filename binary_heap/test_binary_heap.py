import unittest
from binary_heap import *


class BinaryHeapTestCase(unittest.TestCase):
    '''Tests binary_heap.py'''

    def test_constructor(self):
        '''Tests that the Heap constructor creates a Heap object'''
        test_heap = Heap()
        self.assertIsInstance(test_heap, Heap)

    def test_push(self):
        '''Tests that push() adds a value at index 1'''
        test_heap = Heap()
        test_heap.push(1)
        self.assertTrue(test_heap.contents[1] == 1)

    def test_populate(self):
        '''Tests that populate() pushes a list of values'''
        test_heap = Heap()
        test_heap.populate([3, 2, 1])
        self.assertTrue(test_heap.contents == [None, 3, 2, 1])

    def test_pop(self):
        '''Tests that pop() removes and returns the value at index 1'''
        test_heap = Heap()
        test_heap.populate([3, 2, 1])
        return_list = []
        return_list.append(test_heap.pop())
        return_list.append(test_heap.pop())
        return_list.append(test_heap.pop())
        self.assertTrue(return_list == [3, 2, 1] and test_heap.contents == [None])

    def test_pop_empty(self):
        '''Tests that pop() does nothing and doesn't throw an error on an empty heap'''
        test_heap = Heap()
        test_heap.pop()
        self.assertTrue(test_heap.contents == [None])

    def test_sort(self):
        '''Tests that the heap sorts as expected as numbers are added'''
        test_heap = Heap()
        test_heap.populate([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.contents == [None, 5, 4, 2, 1, 3])

    def test_in_out(self):
        '''Tests that an unsorted list put into a heap will be returned in order'''
        test_heap = Heap()
        test_heap.populate([6, 1, 3, 4, 9, 8, 10, 2, 5, 7])
        return_list = []
        for i in range(10):
            return_list.append(test_heap.pop())
        self.assertTrue(return_list == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_peek(self):
        '''Tests that peek() shows the top element'''
        test_heap = Heap()
        test_heap.push(1)
        self.assertTrue(test_heap.peek() == 1)

    def test_peek_empty(self):
        '''Tests that peek() on an empty heap returns None'''
        test_heap = Heap()
        self.assertTrue(test_heap.peek() is None)
