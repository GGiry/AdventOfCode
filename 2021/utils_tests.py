import unittest

from src.utils import read_input_str


class MyTestCase(unittest.TestCase):
    def test_read_input(self):
        input_lines = read_input_str("input_test.txt")
        self.assertEqual(5, len(input_lines))
        self.assertEqual(["4948\n", "4952\n", "4964\n", "4960\n", "4962\n"], input_lines)
