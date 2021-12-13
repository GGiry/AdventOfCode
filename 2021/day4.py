import unittest

from utils import read_input_str


class BingoGrid:
    def __init__(self, grid_str: str):
        self.grid = [[0 for _ in range(5)] for _ in range(5)]

        for i, line in enumerate(grid_str.split("\n")):
            for j, item in enumerate(line.split()):
                self.grid[i][j] = int(item)

    def play(self, number):
        for i, line in enumerate(self.grid):
            for j, item in enumerate(line):
                if item == number:
                    self.grid[i][j] = -1

    def is_winning(self):
        for line in self.grid:
            if line == [-1, -1, -1, -1, -1]:
                return True

        for j in range(len(self.grid[0])):
            if self.grid[0][j] == -1 and self.grid[1][j] == -1 and self.grid[2][j] == -1 and self.grid[3][j] == -1 and \
                    self.grid[4][j] == -1:
                return True

        return False

    def compute_score(self):
        sum_of_elements = 0
        for line in self.grid:
            for item in line:
                if item != -1:
                    sum_of_elements += item
        return sum_of_elements

    def __str__(self):
        return str(self.grid)


def get_numbers_and_boards(input_str):
    numbers_str = input_str[0]

    numbers = [int(num) for num in numbers_str.split(',')]

    grids_str = input_str[1:]

    grids = []
    i = 0
    while i < len(grids_str):
        if grids_str[i] == "":
            i += 1
            continue

        grids.append(
            BingoGrid(
                grids_str[i] + "\n" + grids_str[i + 1] + "\n" + grids_str[i + 2] + "\n" + grids_str[i + 3] + "\n" +
                grids_str[i + 4] + "\n"))

        i += 5

    return numbers, grids


class Day4(unittest.TestCase):

    def test_init_bingo_grid(self):
        bingo_grid = BingoGrid(
            "22 13 17 11  0\n" + " 8  2 23  4 24\n" + "21  9 14 16  7\n" + " 6 10  3 18  5\n" + " 1 12 20 15 19\n")

        self.assertEqual(22, bingo_grid.grid[0][0])
        self.assertEqual(2, bingo_grid.grid[1][1])
        self.assertEqual(14, bingo_grid.grid[2][2])
        self.assertEqual(18, bingo_grid.grid[3][3])
        self.assertEqual(19, bingo_grid.grid[4][4])

    def test_input(self):
        numbers, grids = get_numbers_and_boards(read_input_str("input_day_4_example.txt"))
        self.assertEqual(
            [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1], numbers)

        self.assertEqual(14, grids[0].grid[2][2])
        self.assertEqual(7, grids[1].grid[2][2])
        self.assertEqual(23, grids[2].grid[2][2])

    def test_example(self):
        numbers, grids = get_numbers_and_boards(read_input_str("input_day_4_example.txt"))
        for number in numbers:
            for grid in grids:
                grid.play(number)
                if grid.is_winning():
                    self.assertEqual(4512, number * grid.compute_score())
                    return

    def test_input(self):
        numbers, grids = get_numbers_and_boards(read_input_str("input_day_4.txt"))
        for number in numbers:
            for grid in grids:
                grid.play(number)
                if grid.is_winning():
                    self.assertEqual(31424, number * grid.compute_score())
                    return

    def test_input_2(self):
        numbers, grids = get_numbers_and_boards(read_input_str("input_day_4.txt"))
        for number in numbers:
            for grid in grids:
                grid.play(number)
                if grid.is_winning():
                    if len(grids) > 1:
                        grids.remove(grid)
                    else:
                        self.assertEqual(23042, number * grid.compute_score())
                        return
