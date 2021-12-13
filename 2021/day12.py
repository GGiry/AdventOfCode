import unittest
from typing import List

from utils import read_input_str


class CaveSystem:
    def __init__(self, paths):
        pass

    def count_paths(self):
        pass


class Day12(unittest.TestCase):
    def test_example_1_1(self):
        paths = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
        caves = CaveSystem(paths)
        self.assertEqual(10, caves.count_paths())
