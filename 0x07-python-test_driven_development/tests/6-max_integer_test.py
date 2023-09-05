#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_int(self):
        """max integer"""
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-2, -3, -4, -5]), -2)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([0]), 0)

    def test_error(self):
        """test errors"""
        self.assertRaises(TypeError, max_integer, ["python", 5])

    def test_empty(self):
        """test empty"""
        self.assertIsNone(max_integer([]))
