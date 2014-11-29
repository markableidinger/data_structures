import unittest
from hash import *

def ordinal_value(string):
    total = 0
    for char in string:
        total += ord(char)
    return total


class HashTestCase(unittest.TestCase):
    '''Tests for hash.py'''

# Happy Test Cases
    def test_constructor(self):
        '''Tests that the constructor creates the correct object'''
        test_hash = Hash_Table(1024)
        self.assertIsInstance(test_hash, Hash_Table)

    def test_set(self):
        '''Tests that set() adds a key/value pair as expected'''
        test_hash = Hash_Table(1024)
        test_hash.set('a', 'test')
        expected_value = ord('a') % 1024
        self.assertTrue(test_hash.contents[expected_value]['a'] == 'test')

    def test_lookup(self):
        '''Tests that lookup() returns the correct value'''
        test_hash = Hash_Table(1024)
        test_hash.set('a', 'test')
        self.assertTrue(test_hash.lookup('a') == 'test')

    def test_set_large_string(self):
        '''Tests that the hash function works when the ordinal value
                of the string is over the Hash Table's size'''
        test_hash = Hash_Table(1024)
        test_hash.set('abcdefghijklmnopqrstuvwxyz', 'test')
        expected_value = ordinal_value('abcdefghijklmnopqrstuvwxyz') % 1024
        self.assertTrue(test_hash.contents.get(expected_value, False))

    def test_multiple_key_bucket(self):
        '''Tests that lookup() and set() still work
            when 2 values go into the same bucket'''
        test_hash = Hash_Table(1024)
        test_hash.set('ac', 'test1')
        test_hash.set('bb', 'test2')
        self.assertTrue(test_hash.hash('ac') == test_hash.hash('bb'))
        self.assertTrue(test_hash.lookup('ac') == 'test1')
        self.assertTrue(test_hash.lookup('bb') == 'test2')

#Error Tests
    def test_non_string_inputs(self):
        '''Tests that multiple non-string types of input
                raise appropriate errors'''
        test_hash = Hash_Table(1024)
        with self.assertRaises(TypeError) as context:
            test_hash.set(True, 1)
        with self.assertRaises(TypeError) as context:
            test_hash.set(None, 1)
        with self.assertRaises(TypeError) as context:
            test_hash.set(123, 1)
        with self.assertRaises(TypeError) as context:
            test_hash.set(Hash_Table(1024), 1)
        with self.assertRaises(TypeError) as context:
            test_hash.lookup(True, 1)
        with self.assertRaises(TypeError) as context:
            test_hash.lookup(None, 1)
        with self.assertRaises(TypeError) as context:
            test_hash.lookup(123, 1)
        with self.assertRaises(TypeError) as context:
            test_hash.lookup(Hash_Table(1024), 1)
        test_hash.set('', 'test')
        self.assertTrue(test_hash.lookup('') == 'test')

    def test_lookup_nonexistent(self):
        '''Tests that lookup() raises appropriate error
                if you search for a nonexistent key'''
        test_hash = Hash_Table(1024)
        test_hash.set('ac', 'test')
        print(test_hash.contents)
        with self.assertRaises(ValueError) as context:
            test_hash.lookup('bb')
        with self.assertRaises(ValueError) as context:
            test_hash.lookup('abcdefghijklmnopqrstuvwxyz')
        self.assertTrue(test_hash.lookup('ac') == 'test')

#Test a full dictionary
    def test_full_dictionary_lookup(self):
        test_hash = Hash_Table(1000000)
        file = open('words')
        for line in file:
            test_hash.set(line, line)
        for line in file:
            self.assertTrue(test_hash.lookup(line) == line)
