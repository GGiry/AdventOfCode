import unittest
from utils import read_input_str


def compute_best_position(submarine_positions):
    best = round(sum(submarine_positions) / len(submarine_positions))
    best_value = compute_cost_of_position(best, submarine_positions)
    best_value_next = compute_cost_of_position(best + 1, submarine_positions)
    best_value_prev = compute_cost_of_position(best - 1, submarine_positions)

    if best_value < best_value_next and best_value < best_value_prev:
        return best

    if best_value_prev < best_value < best_value_next:
        while best >= 0 and best_value_prev < best_value:
            best = best - 1
            best_value = compute_cost_of_position(best, submarine_positions)
            best_value_prev = compute_cost_of_position(best - 1, submarine_positions)
        return best
    else:
        while best < len(submarine_positions) and best_value < best_value_next:
            best = best - 1
            best_value = compute_cost_of_position(best, submarine_positions)
            best_value_next = compute_cost_of_position(best - 1, submarine_positions)
        return best


def compute_cost_of_position(goal, positions):
    result = 0
    for position in positions:
        result += abs(goal - position)
    return result


def compute_best_position_2(submarine_positions):
    best = round(sum(submarine_positions) / len(submarine_positions))
    best_value = compute_cost_of_position_2(best, submarine_positions)
    best_value_next = compute_cost_of_position_2(best + 1, submarine_positions)
    best_value_prev = compute_cost_of_position_2(best - 1, submarine_positions)

    if best_value < best_value_next and best_value < best_value_prev:
        return best

    if best_value_prev < best_value < best_value_next:
        while best >= 0 and best_value_prev < best_value:
            best = best - 1
            best_value = compute_cost_of_position_2(best, submarine_positions)
            best_value_prev = compute_cost_of_position_2(best - 1, submarine_positions)
        return best
    else:
        while best < len(submarine_positions) and best_value < best_value_next:
            best = best - 1
            best_value = compute_cost_of_position_2(best, submarine_positions)
            best_value_next = compute_cost_of_position_2(best - 1, submarine_positions)
        return best


def compute_cost_of_position_2(goal, positions):
    result = 0
    for position in positions:
        result += sum(range(abs(goal - position) + 1))
    return result


def compute_best_position_and_get_cost(submarine_positions):
    return compute_cost_of_position(compute_best_position(submarine_positions), submarine_positions)


def compute_best_position_and_get_cost_2(submarine_positions):
    return compute_cost_of_position_2(compute_best_position_2(submarine_positions), submarine_positions)


class Day7(unittest.TestCase):
    def test_compute_best_position(self):
        input_example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(2, compute_best_position(input_example))

    def test_compute_cost(self):
        input_example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(37, compute_cost_of_position(2, input_example))
        self.assertEqual(39, compute_cost_of_position(3, input_example))
        self.assertEqual(41, compute_cost_of_position(4, input_example))
        self.assertEqual(45, compute_cost_of_position(5, input_example))
        self.assertEqual(49, compute_cost_of_position(6, input_example))

    def test_example_1(self):
        input_example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(37, compute_best_position_and_get_cost(input_example))

    def prepare_data(self, path):
        result = []
        list_str = read_input_str(path)
        numbers_str = list_str[0].split(",")
        for number_str in numbers_str:
            result.append(int(number_str))
        return result

    def test_input_1(self):
        input_data = self.prepare_data("input_day_7.txt")
        self.assertEqual(352254, compute_best_position_and_get_cost(input_data))

    def test_compute_cost_of_position_2(self):
        submarines = [1]
        self.assertEqual(0, compute_cost_of_position_2(1, submarines))
        self.assertEqual(1, compute_cost_of_position_2(2, submarines))
        self.assertEqual(3, compute_cost_of_position_2(3, submarines))

    def test_example_2(self):
        input_example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(168, compute_best_position_and_get_cost_2(input_example))

    def test_input_2(self):
        input_data = self.prepare_data("input_day_7.txt")
        self.assertEqual(99053143, compute_best_position_and_get_cost_2(input_data))