import unittest
import base_convert
import os

class BaseConvertTest(unittest.TestCase):
    def test_base_convert_error(self):
        with self.assertRaises(ValueError):
            base_convert.base_convert(10,1)
    def test_palindrome_check_error(self):
        with self.assertRaises(ValueError):
            base_convert.palindrome_check(-3)
    def test_base_convert_edge(self):
        self.assertEqual(base_convert.base_convert(2,2), ['1','0'])
    def test_palindrome_check_edge(self):
        # Could use StringIO or something to mock a file write
        pass

if __name__ == "__main__":
    unittest.main()
