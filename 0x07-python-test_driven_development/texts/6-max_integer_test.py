import unittest
from max_integer import  max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test for empty list
        self.assertEqual(max_integer([]), None)

        # Test for list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test for list of negative integers
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)


if __name__ == '__main__':
    unittest.main()
