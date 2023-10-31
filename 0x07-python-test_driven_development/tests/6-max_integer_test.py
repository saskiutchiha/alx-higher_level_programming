#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        resu = max_integer([3,2,4,57,6])
        self.assertEqual(resu,57)
        self.assertEqual(max_integer([3,2,4,57,100]),100)
        self.assertEqual(max_integer(),None)
        self.assertEqual(max_integer([-11,-3,0,-1,-3]),0)


