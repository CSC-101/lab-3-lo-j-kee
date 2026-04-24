import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)
# test_double_one worked prior to fixing functions.double, but it was only a coincidence.

    def test_double_two(self):
        result = functions.double(3)
# functions.double was originally n*n, when it should be n*2.
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
