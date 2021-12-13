import unittest

from utils import read_input_str


def binary_diagnostic(input_list):
    bit_count = len(input_list[0])

    ones = [0 for _ in range(bit_count)]
    zeroes = [0 for _ in range(bit_count)]

    for item in input_list:
        for i, char in enumerate(item):
            if char == "\n":
                continue
            if char == "0":
                zeroes[i] += 1
            else:
                ones[i] += 1

    gamma = ""
    epsilon = ""
    for i in range(len(ones)):
        if ones[i] > zeroes[i]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2), int(epsilon, 2)


def count_most_bit_value_in_n_position(input_list, n):
    one = 0
    zero = 0

    for item in input_list:
        char = item[n]
        if char == "\n":
            return None
        if char == "0":
            zero += 1
        else:
            one += 1

    if zero > one:
        return 0
    else:
        return 1


def filter_at_position(input_list, n, discriminant):
    result = []

    for i in input_list:
        if i[n] == discriminant:
            result.append(i)

    return result


def binary_diagnostic_oxygen(input_list):
    rating_str = ""
    bit_count = len(input_list[0])

    new_list = input_list
    for i in range(bit_count):
        result = count_most_bit_value_in_n_position(new_list, i)
        rating_str += str(result)
        new_list = filter_at_position(new_list, i, str(result))

    return int(rating_str, 2)


def binary_diagnostic_co2(input_list):
    rating_str = ""
    bit_count = len(input_list[0])

    new_list = input_list
    for i in range(bit_count):
        result = count_most_bit_value_in_n_position(new_list, i)
        result = abs(result - 1)
        rating_str += str(result)
        new_list = filter_at_position(new_list, i, str(result))
        if len(new_list) == 1:
            return int(new_list[0], 2)


def binary_diagnostic_2(input_list):
    return binary_diagnostic_oxygen(input_list), binary_diagnostic_co2(input_list)


class Day3(unittest.TestCase):

    def test_example_1(self):
        input_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                      "01010"]

        gamma, epsilon = binary_diagnostic(input_list)
        self.assertEqual(gamma, 22)
        self.assertEqual(epsilon, 9)

    def test_input_1(self):
        gamma, epsilon = binary_diagnostic(read_input_str("input_day_3.txt"))
        self.assertEqual(2035764, gamma * epsilon)

    def test_example_2(self):
        input_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                      "01010"]

        gamma, epsilon = binary_diagnostic_2(input_list)
        self.assertEqual(gamma, 23)
        self.assertEqual(epsilon, 10)

    def test_input_2(self):
        gamma, epsilon = binary_diagnostic_2(read_input_str("input_day_3.txt"))
        self.assertEqual(2817661, gamma * epsilon)

    def test_count_most_bit_value_in_n_position(self):
        input_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                      "01010"]
        self.assertEqual(1, count_most_bit_value_in_n_position(input_list, 0))
