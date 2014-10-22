import unittest
from queue import *


class QueueTestCase(unittest.TestCase):
    """Tests for `queue.py`."""

    def test_constructor(self):
        """Tests that the constructor makes a Queue object"""
        test_queue = Queue()
        self.assertIsInstance(test_queue, Queue)

    def test_enqueue(self):
        '''Tests that enqueue adds an object as the head of the queue'''
        test_queue = Queue()
        test_queue.enqueue(1)
        self.assertTrue(test_queue.head.value == 1)

    def test_peek(self):
        '''Tests that peek returns the head but does not delete it'''
        test_queue = Queue()
        test_queue.enqueue(1)
        test_queue.enqueue(2)
        test_queue.enqueue(3)
        peek_list = []
        peek_list.append(test_queue.peek())
        peek_list.append(test_queue.peek())
        peek_list.append(test_queue.peek())
        self.assertTrue(peek_list == [1, 1, 1])

    def test_dequeue(self):
        '''Tests that dequeue returns the head and removes it from the queue'''
        test_queue = Queue()
        test_queue.enqueue(1)
        test_queue.enqueue(2)
        test_queue.enqueue(3)
        dequeue_list = []
        dequeue_list.append(test_queue.dequeue())
        dequeue_list.append(test_queue.dequeue())
        dequeue_list.append(test_queue.dequeue())
        self.assertTrue(dequeue_list == [1, 2, 3])

    def test_empty_peek(self):
        '''Tests that peek does not cause an error on an empty queue'''
        test_queue = Queue()
        self.assertTrue(test_queue.peek() is None)

    def test_empty_dequeue(self):
        '''Tests that dequeue does not cause an error on an empty queue'''
        test_queue = Queue()
        self.assertTrue(test_queue.dequeue() is None)


if __name__ == '__main__':
    unittest.main()
