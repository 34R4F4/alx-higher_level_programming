#!/usr/bin/python3
"""
Defines a TestMaxInteger class for testing the max_integer([...]) function.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for the max_integer function.
    """

    def test_positive_integers(self):
        """Test case for positive integers."""
        test_list1 = [1, 2, 3, 4]
        test_list2 = [4, 1, 2, 3]
        test_list3 = [1, 2, 4, 2, 3]

        self.assertEqual(max_integer(test_list1), 4)
        self.assertEqual(max_integer(test_list2), 4)
        self.assertEqual(max_integer(test_list3), 4)

    def test_negative_integers(self):
        """Test case for negative integers."""
        test_list1 = [-91, -31, -4, -2]
        test_list2 = [-2, -91, -31, -4]
        test_list3 = [-91, -123, -2, -31, -4]

        self.assertEqual(max_integer(test_list1), -2)
        self.assertEqual(max_integer(test_list2), -2)
        self.assertEqual(max_integer(test_list3), -2)

    def test_pos_neg_integers(self):
        """Test case for positive and negative integers."""
        test_list = [-9, -14, 23, 98, 0, -9, -100, -1]
        self.assertEqual(max_integer(test_list), 98)

    def test_empty_list(self):
        """Test case for an empty list."""
        test_list = []
        self.assertIsNone(max_integer(test_list))

    def test_one_arg(self):
        """Test case for passing one number to the list."""
        test_list = [1]
        self.assertEqual(max_integer(test_list), 1)

    def test_none_argument(self):
        """Test case for passing None."""
        with self.assertRaises(TypeError):
            max_integer(None)

    # Other test cases omitted for brevity...


if __name__ == '__main__':
    unittest.main()
