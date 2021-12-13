import unittest
from utils import read_input_str


def prepare_data(a_path):
    lines = []
    lines_str = read_input_str(a_path)
    for line_str in lines_str:
        line = []
        for char in line_str:
            line.append(int(char))
        lines.append(line)
    return lines


def find_lower_adjacent(a_heightmap, a_coordinate):
    current_value = a_heightmap[a_coordinate[0]][a_coordinate[1]]
    if a_coordinate[0] > 0 and a_heightmap[a_coordinate[0] - 1][a_coordinate[1]] < current_value:
        return a_coordinate[0] - 1, a_coordinate[1]

    if a_coordinate[1] > 0 and a_heightmap[a_coordinate[0]][a_coordinate[1] - 1] < current_value:
        return a_coordinate[0], a_coordinate[1] - 1

    if a_coordinate[0] < len(a_heightmap) - 1 and a_heightmap[a_coordinate[0] + 1][a_coordinate[1]] < current_value:
        return a_coordinate[0] + 1, a_coordinate[1]

    if a_coordinate[1] < len(a_heightmap[0]) - 1 and a_heightmap[a_coordinate[0]][a_coordinate[1] + 1] < current_value:
        return a_coordinate[0], a_coordinate[1] + 1

    return a_coordinate


def is_lowest_of_adjacent(a_heightmap, a_coordinate):
    current_value = a_heightmap[a_coordinate[0]][a_coordinate[1]]
    if a_coordinate[0] > 0 and a_heightmap[a_coordinate[0] - 1][a_coordinate[1]] <= current_value:
        # print(current_value, a_heightmap[param[0] - 1][param[1]])
        return False

    if a_coordinate[1] > 0 and a_heightmap[a_coordinate[0]][a_coordinate[1] - 1] <= current_value:
        # print(current_value, a_heightmap[param[0]][param[1] - 1])
        return False

    if a_coordinate[0] < len(a_heightmap) - 1 and a_heightmap[a_coordinate[0] + 1][a_coordinate[1]] <= current_value:
        # print(current_value, a_heightmap[param[0] + 1][param[1]])
        return False

    if a_coordinate[1] < len(a_heightmap[0]) - 1 and a_heightmap[a_coordinate[0]][a_coordinate[1] + 1] <= current_value:
        # print(current_value, a_heightmap[param[0]][param[1] + 1])
        return False

    return True


def find_low_points_coordinates(a_heightmap):
    result = []
    for i, line in enumerate(a_heightmap):
        for j, item in enumerate(line):
            if is_lowest_of_adjacent(a_heightmap, (i, j)):
                result.append((i, j))
    return result


def find_low_points(a_heightmap):
    result = []
    coordinates = find_low_points_coordinates(a_heightmap)
    for coordinate in coordinates:
        result.append(a_heightmap[coordinate[0]][coordinate[1]])
    return result


def find_source(a_heightmap, coordinate):
    new_coordinates = find_lower_adjacent(a_heightmap, coordinate)
    while coordinate != new_coordinates:
        coordinate = new_coordinates
        new_coordinates = find_lower_adjacent(a_heightmap, coordinate)

    return coordinate


def find_basins(a_heightmap):
    result = {}
    coordinates = find_low_points_coordinates(a_heightmap)
    for coordinate in coordinates:
        result[coordinate] = 0

    for i, line in enumerate(a_heightmap):
        for j, point in enumerate(line):
            if point != 9:
                source = find_source(a_heightmap, (i, j))
                result[source] += 1

    return list(result.values())


class Day9(unittest.TestCase):
    def test_data_prepare(self):
        heightmap = prepare_data("input_day_9_example.txt")
        self.assertEqual(10, len(heightmap[0]))
        self.assertEqual(5, len(heightmap))
        self.assertEqual(2, heightmap[0][0])
        self.assertEqual(2, heightmap[0][0])
        self.assertEqual(1, heightmap[0][1])
        self.assertEqual(3, heightmap[1][0])

    def test_example(self):
        heightmap = prepare_data("input_day_9_example.txt")
        low_points = find_low_points(heightmap)
        self.assertEqual([1, 0, 5, 5], low_points)
        self.assertEqual(15, sum(low_points) + len(low_points))

    def test_input(self):
        heightmap = prepare_data("input_day_9.txt")
        low_points = find_low_points(heightmap)
        self.assertEqual(528, sum(low_points) + len(low_points))

    def test_example_2(self):
        heightmap = prepare_data("input_day_9_example.txt")
        basins = find_basins(heightmap)
        basins.sort()
        self.assertEqual(1134, basins[-3] * basins[-2] * basins[-1])

    def test_input_2(self):
        heightmap = prepare_data("input_day_9.txt")
        basins = find_basins(heightmap)
        basins.sort()
        self.assertEqual(920448, basins[-3] * basins[-2] * basins[-1])
