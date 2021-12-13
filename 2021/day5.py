import unittest
from typing import List

from utils import read_input_str


class Point:
    def __init__(self, in_str: str):
        values = in_str.split(",")
        self.x = int(values[0])
        self.y = int(values[1])

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __lt__(self, other):
        if self.x <= other.x and self.y <= other.y:
            return True
        return False


class Line:
    def __init__(self, str_representation: str):
        points = str_representation.split("->")

        self.start = Point(points[0])
        self.finish = Point(points[1])

    def __str__(self):
        return f"{self.start} -> {self.finish}"

    def is_horizontal_or_vertical(self):
        if self.start.x == self.finish.x or self.start.y == self.finish.y:
            return True
        return False


def find_max_x(vertices: List[Line]):
    max_x = 0
    for vertex in vertices:
        if max_x < vertex.start.x:
            max_x = vertex.start.x
        if max_x < vertex.finish.x:
            max_x = vertex.finish.x
    return max_x


def find_max_y(vertices):
    max_y = 0
    for vertex in vertices:
        if max_y < vertex.start.y:
            max_y = vertex.start.y
        if max_y < vertex.finish.y:
            max_y = vertex.finish.y
    return max_y


class Vents:
    def __init__(self, lines: List[Line]):
        max_x = find_max_x(lines) + 1
        max_y = find_max_y(lines) + 1
        self.grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

        for line in lines:
            min_x = min(line.start.x, line.finish.x)
            max_x = max(line.start.x, line.finish.x)
            min_y = min(line.start.y, line.finish.y)
            max_y = max(line.start.y, line.finish.y)

            if line.is_horizontal_or_vertical():
                for i in range(min_x, max_x + 1):
                    for j in range(min_y, max_y + 1):
                        self.grid[j][i] += 1
            else:
                direction = [0, 0]
                if line.start.x < line.finish.x:
                    direction[1] = 1
                else:
                    direction[1] = -1

                if line.start.y < line.finish.y:
                    direction[0] = 1
                else:
                    direction[0] = -1

                for i in range(max_x - min_x + 1):
                    self.grid[line.start.y + (i * direction[0])][line.start.x + (i * direction[1])] += 1

    def __str__(self):
        result = ""

        for line in self.grid:
            for item in line:
                if item == 0:
                    result += "."
                else:
                    result += str(item)
            result += "\n"

        return result

    def count_overlaps(self):
        result = 0
        for row in self.grid:
            for item in row:
                if item > 1:
                    result += 1
        return result


class MyTestCase(unittest.TestCase):

    def get_lines(self, path):
        return [Line(line) for line in read_input_str(path)]

    def filter_diagonal_out(self, lines):
        result = []
        for line in lines:
            if line.is_horizontal_or_vertical():
                result.append(line)
        return result

    def test_vertex_init(self):
        line = Line("0,9 -> 5,9")
        self.assertEqual(0, line.start.x)
        self.assertEqual(9, line.start.y)
        self.assertEqual(5, line.finish.x)
        self.assertEqual(9, line.finish.y)

    def test_vents_init(self):
        line = Line("1,1 -> 3,1")
        vents = Vents([line])
        self.assertEqual("....\n" + ".111\n", str(vents))

    def test_vents_example(self):
        lines = self.get_lines("input_day_5_example.txt")
        lines_horizontal_and_verticals = self.filter_diagonal_out(lines)
        vents = Vents(lines_horizontal_and_verticals)
        self.assertEqual(
            ".......1..\n" + "..1....1..\n" + "..1....1..\n" + ".......1..\n" + ".112111211\n" + "..........\n" +
            "..........\n" + "..........\n" + "..........\n" + "222111....\n", str(vents))

    def test_vents_example_step_2(self):
        lines = self.get_lines("input_day_5_example.txt")
        vents = Vents(lines)
        self.assertEqual(
            "1.1....11.\n" + ".111...2..\n" + "..2.1.111.\n" + "...1.2.2..\n" + ".112313211\n" + "...1.2....\n" +
            "..1...1...\n" + ".1.....1..\n" + "1.......1.\n" + "222111....\n", str(vents))

    def test_example(self):
        lines = self.get_lines("input_day_5_example.txt")
        lines_horizontal_and_verticals = self.filter_diagonal_out(lines)
        vents = Vents(lines_horizontal_and_verticals)
        self.assertEqual(5, vents.count_overlaps())

    def test_example_step_2(self):
        lines = self.get_lines("input_day_5_example.txt")
        vents = Vents(lines)
        self.assertEqual(12, vents.count_overlaps())

    def test_step_1(self):
        lines = self.get_lines("input_day_5.txt")
        lines_horizontal_and_verticals = self.filter_diagonal_out(lines)
        vents = Vents(lines_horizontal_and_verticals)
        self.assertEqual(7380, vents.count_overlaps())

    def test_step_2(self):
        lines = self.get_lines("input_day_5.txt")
        vents = Vents(lines)
        self.assertEqual(21373, vents.count_overlaps())
