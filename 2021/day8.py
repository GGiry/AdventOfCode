import unittest
from collections import Sized
from typing import List

from utils import read_input_str

"""
0: NA
1: NA
2: 1
3: 7
4: 4
5: 2, 3, 5
6: 0, 6, 9
7 : 8

 _
|_|
|_|

Barre du haut = 7 - 1
Barre bas gauche = 8 - 9
Barre du bas = 9-4-Barre du haut

Barre du milieu = 8 - 0
Barre haut gauche = 8 - 6
Barre bas droite = 8 - 2 - Barre bas gauche
Barre haut gauche = 8 - 5 - Barre haut gauche
"""


class SegmentDigits(Sized):
    def __len__(self) -> int:
        return len(self.light_up)

    def __init__(self, initial_input):
        self.light_up = {}
        for char in initial_input:
            self.light_up[ord(char) - ord('a')] = 1

    def __sub__(self, other):
        return set(self.light_up.keys()).difference(set(other.light_up.keys()))

    def __repr__(self):
        return f"{len(self)} {self.light_up.keys()}"

    def __eq__(self, other):
        return self.light_up.keys() == other.light_up.keys()


class Puzzle:
    def __init__(self, initial_input):
        self.numbers = {}
        self.pattern = []
        self.output = []
        unique_patterns_str, four_digit_output_str = initial_input.split("|")

        for pattern in unique_patterns_str.split(" "):
            self.pattern.append(SegmentDigits(pattern.replace(" ", "")))

        for output in four_digit_output_str.split(" "):
            self.output.append(SegmentDigits(output.replace(" ", "")))

        for pattern in self.pattern:
            if len(pattern) == 2:
                self.numbers[1] = pattern
            if len(pattern) == 3:
                self.numbers[7] = pattern
            if len(pattern) == 4:
                self.numbers[4] = pattern
            if len(pattern) == 7:
                self.numbers[8] = pattern

        for pattern in self.pattern:
            if len(pattern) == 6 and len(pattern - self.numbers[4]) == 2:
                self.numbers[9] = pattern
                break

    def get(self, an_int):
        return self.numbers[an_int]

    def solve(self):
        for pattern in self.pattern:
            if len(pattern) == 5 and len(pattern - self.numbers[9]) == 1:
                self.numbers[2] = pattern
                break

        for pattern in self.pattern:
            if len(pattern) == 5 and len(pattern - self.numbers[2]) == 1:
                self.numbers[3] = pattern
                break

        for pattern in self.pattern:
            if len(pattern) == 5 and len(pattern - self.numbers[2]) == 2:
                self.numbers[5] = pattern
                break

        for pattern in self.pattern:
            if len(pattern) == 6 and pattern != self.numbers[9] and len(pattern - self.numbers[5]) == 2:
                self.numbers[0] = pattern
                break

        for pattern in self.pattern:
            if len(pattern) == 6 and pattern != self.numbers[9] and len(pattern - self.numbers[5]) == 1:
                self.numbers[6] = pattern
                break

        result = ""
        for output in self.output:
            if self.numbers[0] == output:
                result += "0"
            if self.numbers[1] == output:
                result += "1"
            if self.numbers[2] == output:
                result += "2"
            if self.numbers[3] == output:
                result += "3"
            if self.numbers[4] == output:
                result += "4"
            if self.numbers[5] == output:
                result += "5"
            if self.numbers[6] == output:
                result += "6"
            if self.numbers[7] == output:
                result += "7"
            if self.numbers[8] == output:
                result += "8"
            if self.numbers[9] == output:
                result += "9"

        return int(result)


def prepare_data(in_str: str):
    unique_patterns_str, four_digit_output_str = in_str.split("|")
    return [""], four_digit_output_str.split(" ")


def count_easy(digits: List[str]):
    result = 0
    for digit in digits:
        if len(digit) in [2, 3, 4, 7]:
            result += 1
    return result


class Day8(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_prepare_data(self):
        input_str = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

    def test_example_1_1(self):
        input_str = "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"
        _, output = prepare_data(input_str)
        self.assertEqual(3, count_easy(output))

    def test_exemple_1(self):
        inputs_str = read_input_str("input_day_8_example.txt")
        count_all = 0
        for input_str in inputs_str:
            _, output = prepare_data(input_str)
            count_all += count_easy(output)
        self.assertEqual(26, count_all)

    def test_input_1(self):
        inputs_str = read_input_str("input_day_8.txt")
        count_all = 0
        for input_str in inputs_str:
            _, output = prepare_data(input_str)
            count_all += count_easy(output)
        self.assertEqual(0, count_all)

    def test_example_2_1(self):
        input_str = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        puzzle = Puzzle(input_str)
        self.assertEqual(5353, puzzle.solve())

    def test_exemple_2(self):
        inputs_str = read_input_str("input_day_8_example.txt")
        count_all = 0
        for input_str in inputs_str:
            puzzle = Puzzle(input_str)
            count_all += puzzle.solve()
        self.assertEqual(61229, count_all)

    def test_input_2(self):
        inputs_str = read_input_str("input_day_8.txt")
        count_all = 0
        for input_str in inputs_str:
            puzzle = Puzzle(input_str)
            count_all += puzzle.solve()
        self.assertEqual(987553, count_all)
