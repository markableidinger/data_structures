import random
import unittest
from binary_tree import *


class binTreeTestCase(unittest.TestCase):
    '''Tests for binary_tree.py'''

    def test_constructor(self):
        test_tree = Binary_Tree()
        self.assertIsInstance(test_tree, Binary_Tree)

    def test_insert(self):
        test_tree = Binary_Tree()
        test_tree.insert(5)
        self.assertTrue(test_tree.head.value == 5)

    def test_multiple_insert(self):
        test_tree = Binary_Tree()
        test_tree.insert(1)
        test_tree.insert(2)
        test_tree.insert(3)
        test_tree.insert(4)
        test_tree.insert(5)
        test_tree.insert(6)
        test_tree.insert(7)
        self.assertTrue(test_tree.head.value == 1)

    def test_size(self):
        test_tree = Binary_Tree()
        test_tree.insert(2)
        test_tree.insert(3)
        test_tree.insert(4)
        test_tree.insert(5)
        self.assertTrue(test_tree.size() == 4)

    def test_contains(self):
        test_tree = Binary_Tree()
        test_tree.insert(1)
        self.assertTrue(test_tree.contains(1))
        self.assertFalse(test_tree.contains(2))

    def test_single_delete(self):
        test_tree = Binary_Tree()
        test_tree.insert(1)
        self.assertTrue(test_tree.contains(1))
        test_tree.delete(1)
        self.assertFalse(test_tree.contains(1))

    def test_empty_delete(self):
        test_tree = Binary_Tree()
        test_tree.delete(1)
        self.assertTrue(test_tree.head is None)

    def test_populate(self):
        test_tree = Binary_Tree()
        test_tree.populate([5, 3, 7, 1, 9, 8, 4, 2])
        self.assertTrue(test_tree.size() == 8)

    def test_empty_size(self):
        test_tree = Binary_Tree()
        self.assertTrue(test_tree.size() == 0)

    def test_delete_head(self):
        test_tree = Binary_Tree()
        test_tree.populate([2, 1, 3])
        test_tree.delete(2)
        self.assertTrue(test_tree.head.value == 1)
        self.assertTrue(test_tree.head.right.value == 3)
        self.assertTrue(test_tree.head.left is None)

    def test_delete_leaf(self):
        test_tree = Binary_Tree()
        test_tree.populate([2, 1, 3])
        test_tree.delete(1)
        self.assertTrue(test_tree.head.value == 2)
        self.assertTrue(test_tree.head.right.value == 3)
        self.assertTrue(test_tree.head.left is None)

    def test_balance(self):
        test_tree = Binary_Tree()
        test_tree.populate([1, 2, 3, 4, 5])
        self.assertTrue(test_tree.balance() == -4)

    def test_depth(self):
        test_tree = Binary_Tree()
        test_tree.populate([3, 1, 2, 4, 5, 6])
        self.assertTrue(test_tree.depth(test_tree.head) == 4)

    def test_double_insert(self):
        test_tree = Binary_Tree()
        test_tree.insert(1)
        test_tree.insert(1)
        self.assertTrue(test_tree.head.value == 1)
        self.assertTrue(test_tree.head.left is None)
        self.assertTrue(test_tree.head.right is None)

    def test_pre_order(self):
        test_tree = Binary_Tree()
        test_tree.populate([4, 2, 1, 3, 6, 5, 7])
        self.assertTrue(test_tree.listify_pre() == [4, 2, 1, 3, 6, 5, 7])

    def test_in_order(self):
        test_tree = Binary_Tree()
        test_tree.populate([4, 2, 1, 3, 6, 5, 7])
        self.assertTrue(test_tree.listify_in() == [1, 2, 3, 4, 5, 6, 7])

    def test_post_order(self):
        test_tree = Binary_Tree()
        test_tree.populate([4, 2, 1, 3, 6, 5, 7])
        self.assertTrue(test_tree.listify_post() == [1, 3, 2, 5, 7, 6, 4])

    def test_breadth(self):
        test_tree = Binary_Tree()
        test_tree.populate([4, 2, 1, 3, 6, 5, 7])
        self.assertTrue(test_tree.breadth_first(test_tree.head) == [4, 2, 6, 1, 3, 5, 7])

    def test_empty_traversals(self):
        test_tree = Binary_Tree()
        self.assertTrue(test_tree.listify_pre() == [])
        self.assertTrue(test_tree.listify_in() == [])
        self.assertTrue(test_tree.listify_post() == [])
        self.assertTrue(test_tree.breadth_first(test_tree.head) == [])

    def test_empty_depth_balance(self):
        test_tree = Binary_Tree()
        self.assertTrue(test_tree.depth(test_tree.head) == 0)
        self.assertTrue(test_tree.balance() == 0)

    def test_empty_contains(self):
        test_tree = Binary_Tree()
        self.assertFalse(test_tree.contains(1))

    def test_rebalance(self):
        for i in range(50):
            test_tree = Binary_Tree()
            pop_list = make_list()
            test_tree.populate(pop_list)
            test_tree.insert_order()
            print test_tree.balance()
            self.assertTrue(test_tree.balance() <= 1)


def make_list():
    random_list = []
    for i in range(31):
        random_list.append(random.randrange(100))
    return random_list
