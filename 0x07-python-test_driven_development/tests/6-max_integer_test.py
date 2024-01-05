#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "hello"])

    def test_value(self):
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 3)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)

