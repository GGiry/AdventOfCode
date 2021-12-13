import unittest
from typing import List
from utils import read_input_int


def find_value_adding_to_a_equals_n(values, value_a, goal_n):
    for value in values:
        if value_a + value == goal_n:
            return value
    return None


def find_n_elements_summing_to_goal(values: List[int], n: int, goal: int) -> List[int]:
    if n == 1 and goal in values:
        return [goal, ]

    for i, value in enumerate(values):
        result = find_n_elements_summing_to_goal(values[i:], n - 1, goal - value)
        if result:
            return [value] + result

    for i, value in enumerate(values):


    return []


def find_sum_2020(values: List[int]):
    for value in values:
        if 2020 - value in values:
            return value, 2020 - value
    return None


def find_sum_of_3_2020(values):
    pass


class MyTestCase(unittest.TestCase):

    def test_one_element(self):
        result = find_n_elements_summing_to_goal([0], 1, 0)
        self.assertEqual([0], result)

    def test_one_element_absent(self):
        result = find_n_elements_summing_to_goal([0], 1, 1)
        self.assertEqual([], result)

    def test_one_element_list_longer(self):
        result = find_n_elements_summing_to_goal([1, 0], 1, 0)
        self.assertEqual([0], result)

    def test_two_elements(self):
        result = find_n_elements_summing_to_goal([1, 2], 2, 3)
        self.assertEqual([1, 2], result)

    def test_exemple(self):
        values = [1721, 979, 366, 299, 675, 1456]
        result = find_n_elements_summing_to_goal(values, 2, 2020)
        self.assertEqual(1721, result[0])
        self.assertEqual(299, result[1])

    def test_input(self):
        values = read_input_int("input_day_1.txt")
        value_a, value_b = find_n_elements_summing_to_goal(values, 2, 2020)
        self.assertEqual(527, value_a)
        self.assertEqual(1493, value_b)
        print(value_a * value_b)

    def test_exemple_2(self):
        values = [1721, 979, 366, 299, 675, 1456]
        value_a, value_b, value_c = find_sum_of_3_2020(values)
        self.assertEqual(979, value_a)
        self.assertEqual(366, value_b)
        self.assertEqual(675, value_c)
