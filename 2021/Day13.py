import unittest
from typing import List

from utils import read_input_str


class Origami:
    def __init__(self, an_input: List[str]):
        self.folds = []

        coordinates = []
        max_x = 0
        max_y = 0

        for line in an_input:
            if line.strip():
                if line.startswith("fold"):
                    axis, value = line.split(" ")[2].split("=")
                    self.folds.append((axis, int(value)))
                else:
                    x, y = line.split(",")
                    coordinates.append((int(x), int(y)))
                    max_x = max(int(x), max_x)
                    max_y = max(int(y), max_y)

        self.sheet = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for coordinate in coordinates:
            self.sheet[coordinate[1]][coordinate[0]] = "#"

    def fold(self):
        if len(self.folds) > 0:
            fold = self.folds.pop(0)

            if fold[0] == 'y':
                max_x = len(self.sheet[0]) + 1
                max_y = int((len(self.sheet) + 1) / 2)
                sheet = [["." for _ in range(max_x)] for _ in range(max_y)]
                for i in range(max_y):
                    sheet[i] = self.sheet[i]

                for i in range(max_y):
                    for j in range(max_x):
                        sheet[i][j] = self.sheet[i][j], self.sheet[i][j + value]


class Day13(unittest.TestCase):
    def test_init(self):
        origami = Origami(read_input_str("input_day_13_example.txt"))

        self.assertEqual([['.', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.'],
                          ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '#', '.', '.', '.', '.', '#', '.', '#', '#', '.'],
                          ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#'],
                          ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.']],
                         origami.sheet)

        self.assertEqual(2, len(origami.folds))
        self.assertEqual(("y", 7), origami.folds[0])
        self.assertEqual(("x", 5), origami.folds[1])

    def test_fold(self):
        origami = Origami(read_input_str("input_day_13_example.txt"))
        origami.fold()
        self.assertEqual([['#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '.'],
                          ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#'],
                          ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
                          ['.', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']],
                         origami.sheet)
