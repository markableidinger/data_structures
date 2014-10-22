import unittest
from priority_queue import *


class PriorityqTestCase(unittest.TestCase):

    def test_constructor(self):
        """Tests that the constructor makes a Priorityq object"""
        p = Priorityq()
        self.assertIsInstance(p, Priorityq)

    def test_push(self):
        '''Tests that push appends a tuple to Priorityq.contents'''
        p = Priorityq()
        p.push(5, 'value')
        self.assertTrue(p.contents == [None, (5, 'value')])

    def test_bad_priority(self):
        '''Tests that an invalid priority is not added to contents'''
        p = Priorityq()
        p.push('invalid', 'value')
        p.push(109838927387465, 'value')
        p.push(None, 'value')
        p.push(5, 'value')
        self.assertTrue(p.contents == [None, (5, 'value')])

    def test_pop(self):
        '''Tests that pop returns and removes the top priority'''
        p = Priorityq()
        p.push(1, 'value1')
        p.push(2, 'value2')
        popped = p.pop()
        self.assertTrue(popped == (2, 'value2')
            and p.contents[1] == (1, 'value1'))

    def test_peek(self):
        '''Tests that peek returns and doesn't remove the top priority'''
        p = Priorityq()
        p.push(1, 'value')
        p.push(2, 'value2')
        self.assertTrue(p.peek() == (2, 'value2')
            and p.contents[1] == (2, 'value2'))

    def test_peek_pop_empty(self):
        '''Tests that peek and pop work on empty Priorityqs and
            the queue still works'''
        p = Priorityq()
        p.pop()
        p.peek()
        p.push(1, 'value')
        self.assertTrue(p.contents == [None, (1, 'value')])

    def test_populate(self):
        '''Tests that populate pushes a list of tuples'''
        p = Priorityq()
        p.populate([(3, 'value'), (2, 'value2'), (1, 'value3')])
        self.assertTrue(p.contents == [None, (3, 'value'),
            (2, 'value2'), (1, 'value3')])

    def test_sorted_by_priority(self):
        '''Tests that when values are pushed in an unsorted order
            they will be popped sorted by priority'''
        p = Priorityq()
        p.populate([(6, 'P'), (1, 'N'), (4, 'T'), (2, 'O'), (3, 'H'), (5, 'Y')])
        test_string = ''
        for i in range(6):
            test_string += p.pop()[1]
        self.assertTrue(test_string == 'PYTHON')
