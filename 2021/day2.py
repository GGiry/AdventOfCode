import unittest

from submarine import Submarine
from utils import read_input_str


class Day2(unittest.TestCase):

    def test_example_1(self):
        input_str = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        submarine = Submarine()
        submarine.move(input_str)
        self.assertEqual(150, submarine.get_position())

    def test_example_2(self):
        input_str = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        submarine = Submarine()
        submarine.move_aim(input_str)
        self.assertEqual(15, submarine.horizontal)
        self.assertEqual(60, submarine.depth)
        self.assertEqual(900, submarine.get_position())

    def test_part1(self):
        submarine = Submarine()
        submarine.move(read_input_str("input_day_2.txt"))
        self.assertEqual(2091984, submarine.get_position())

    def test_part2(self):
        submarine = Submarine()
        submarine.move_aim(read_input_str("input_day_2.txt"))
        self.assertEqual(2086261056, submarine.get_position())

    def test_forward_only(self):
        submarine = Submarine()
        submarine.move_aim(["forward 5"])
        self.assertEqual(0, submarine.depth)
        self.assertEqual(0, submarine.aim)
        self.assertEqual(5, submarine.horizontal)

    def test_down_only(self):
        submarine = Submarine()
        submarine.move_aim(["down 5"])
        self.assertEqual(0, submarine.depth)
        self.assertEqual(5, submarine.aim)
        self.assertEqual(0, submarine.horizontal)

    def test_forward_down(self):
        submarine = Submarine()
        submarine.move_aim(["forward 5", "down 5"])
        self.assertEqual(0, submarine.depth)
        self.assertEqual(5, submarine.aim)
        self.assertEqual(5, submarine.horizontal)

    def test_forward_down_forward(self):
        submarine = Submarine()
        submarine.move_aim(["forward 5", "down 5", "forward 8"])
        self.assertEqual(40, submarine.depth)
        self.assertEqual(5, submarine.aim)
        self.assertEqual(13, submarine.horizontal)
