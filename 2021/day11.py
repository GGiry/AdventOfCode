import unittest
from typing import List

from utils import read_input_str


class Octopuses:
    def __init__(self, lines):
        self.lines = [[int(value) for value in line] for line in lines]
        self.light_count = 0

    def __repr__(self):
        result = ""
        for line in self.lines:
            for value in line:
                result += str(value)
            result += "\n"
        return result

    def step(self):
        self.increase_all()

        flash_list = []
        light_count_step = -1
        while light_count_step != 0:
            light_count_step = 0
            for i, line in enumerate(self.lines):
                for j, value in enumerate(line):
                    if value > 9:
                        if not (i, j) in flash_list:
                            flash_list.append((i, j))
                            self.increase_neighbours(i, j)
                            light_count_step += 1
            self.light_count += light_count_step

        for coordinates in flash_list:
            self.lines[coordinates[0]][coordinates[1]] = 0

    def increase_all(self):
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                self.lines[i][j] += 1

    def increase_neighbours(self, i, j):
        for a in range(max(i - 1, 0), min(i + 2, len(self.lines))):
            for b in range(max(j - 1, 0), min(j + 2, len(self.lines[0]))):
                if a == i and b == j:
                    continue
                self.lines[a][b] += 1

    def compute_synchronizing_step(self):
        grid_size = len(self.lines) * len(self.lines[0])

        result = 0
        difference = 0
        while difference != grid_size:
            previous_count = self.light_count
            self.step()
            result += 1
            difference = self.light_count - previous_count
        return result


class Day11(unittest.TestCase):
    def test_simple(self):
        before = ["11111", "19991", "19191", "19991", "11111"]
        octopuses = Octopuses(before)
        octopuses.step()
        self.assertEqual("34543\n" + "40004\n" + "50005\n" + "40004\n" + "34543\n", str(octopuses))

    def test_increase_all(self):
        before = ["11111", "19991", "19191", "19991", "11111"]
        octopuses = Octopuses(before)
        octopuses.increase_all()
        self.assertEqual("22222\n" + "21010102\n" + "2102102\n" + "21010102\n" + "22222\n", str(octopuses))

    def test_increase_neighbours(self):
        before = ["111", "111", "111"]
        octopuses = Octopuses(before)
        octopuses.increase_neighbours(1, 1)
        self.assertEqual("222\n" + "212\n" + "222\n", str(octopuses))
        octopuses.increase_neighbours(0, 0)
        self.assertEqual("232\n" + "322\n" + "222\n", str(octopuses))

    def test_init(self):
        octopuses = Octopuses(read_input_str("input_day_11_example.txt"))
        self.assertEqual("5483143223\n" + "2745854711\n" + "5264556173\n" + "6141336146\n" + "6357385478\n" +
                         "4167524645\n" + "2176841721\n" + "6882881134\n" + "4846848554\n" + "5283751526\n",
                         str(octopuses))

    def test_example_1_step_1_2(self):
        octopuses = Octopuses(read_input_str("input_day_11_example.txt"))
        octopuses.step()
        self.assertEqual(
            "6594254334\n" + "3856965822\n" + "6375667284\n" + "7252447257\n" + "7468496589\n" +
            "5278635756\n" + "3287952832\n" + "7993992245\n" + "5957959665\n" + "6394862637\n",
            str(octopuses))
        octopuses.step()
        self.assertEqual(
            "8807476555\n" + "5089087054\n" + "8597889608\n" + "8485769600\n" + "8700908800\n" +
            "6600088989\n" + "6800005943\n" + "0000007456\n" + "9000000876\n" + "8700006848\n",
            str(octopuses))

    def test_example_1(self):
        octopuses = Octopuses(read_input_str("input_day_11_example.txt"))
        for i in range(100):
            octopuses.step()

        self.assertEqual(
            "0397666866\n" + "0749766918\n" + "0053976933\n" + "0004297822\n" + "0004229892\n" +
            "0053222877\n" + "0532222966\n" + "9322228966\n" + "7922286866\n" + "6789998766\n",
            str(octopuses))

        self.assertEqual(1656, octopuses.light_count)

    def test_input_1(self):
        octopuses = Octopuses(read_input_str("input_day_11.txt"))
        for i in range(100):
            octopuses.step()
        self.assertEqual(1743, octopuses.light_count)

    def test_example_2(self):
        octopuses = Octopuses(read_input_str("input_day_11_example.txt"))
        self.assertEqual(195, octopuses.compute_synchronizing_step())

    def test_input_2(self):
        octopuses = Octopuses(read_input_str("input_day_11.txt"))
        self.assertEqual(0, octopuses.compute_synchronizing_step())
