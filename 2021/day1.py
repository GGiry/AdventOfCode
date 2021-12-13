import unittest

from submarine import Radar
from utils import read_input_int


class Day1(unittest.TestCase):

    def test_count_increase_example(self):
        depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        increases = Radar.count_increase(depths)
        self.assertEqual(7, increases)

    def test_count_increase_empty(self):
        depths = []
        increases = Radar.count_increase(depths)
        self.assertEqual(0, increases)

    def test_ignore_decrease(self):
        depths = [200, 199]
        increases = Radar.count_increase(depths)
        self.assertEqual(0, increases)

    def test_count_increase_simple(self):
        depths = [200, 201]
        increases = Radar.count_increase(depths)
        self.assertEqual(1, increases)

    def test_count_increase_sliding_example(self):
        depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        increases = Radar.count_increase_sliding(depths)
        self.assertEqual(5, increases)

    def test_count_increase_sliding_simple(self):
        depths = [199, 200, 208, 210]
        increases = Radar.count_increase_sliding(depths)
        self.assertEqual(1, increases)

    def test_part1(self):
        increases = Radar.count_increase(read_input_int("input_day_1.txt"))
        self.assertEqual(1387, increases)

    def test_part2(self):
        increases = Radar.count_increase_sliding(read_input_int("input_day_1.txt"))
        self.assertEqual(1362, increases)
