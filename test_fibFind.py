from distutils.log import error
import unittest

from fibfind import fibArray


class TestFibonnaciResult(unittest.TestCase):
    def test_number(self):
        self.assertEqual(fibArray(1) == 1),
        self.assertEqual(fibArray(2) == 2),
        self.assertEqual(fibArray(5) == 8)

    # def test_input_type(self):
    #     self.assertTrue(fibArray("some-string") == error)


if __name__ == "__main__":
    unittest.main()


# List of sequence
# https://www.planetmath.org/listoffibonaccinumbers#:~:text=%20%20%20Title%20%20%20list%20of,%20cvalente%20%2811260%29%20%205%20more%20rows%20
