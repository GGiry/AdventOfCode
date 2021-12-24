import collections
import unittest
from typing import List, Tuple

from utils import read_input_str


class Polymer:

    def __init__(self, a_template: str, rules: List[str]):
        self.template = {}
        self.rules = {}

        for i in range(len(a_template)):
            pair = a_template[i:i + 2]
            if len(pair) == 2:
                if pair in self.template:
                    self.template[pair] += 1
                else:
                    self.template[pair] = 1

        for rule in rules:
            pair, element = rule.split(" -> ")
            self.rules[pair] = element

    def step(self, count=1):
        for i in range(count):
            result = {}
            for pair in self.template:
                element = self.rules[pair]
                new_pair_1 = pair[0] + element
                new_pair_2 = element + pair[1]
                if new_pair_1 in result:
                    result[new_pair_1] += self.template[pair]
                else:
                    result[new_pair_1] = self.template[pair]

                if new_pair_2 in result:
                    result[new_pair_2] += self.template[pair]
                else:
                    result[new_pair_2] = self.template[pair]

            self.template = result

    def get_least_and_most_diff(self) -> Tuple[int, int]:
        chars = {}
        first = True
        for pair in self.template:
            if first:
                if pair[0] in chars:
                    chars[pair[0]] += self.template[pair]
                else:
                    chars[pair[0]] = self.template[pair]
                first = False

            if pair[1] in chars:
                chars[pair[1]] += self.template[pair]
            else:
                chars[pair[1]] = self.template[pair]

        return chars[min(chars, key=chars.get)], chars[max(chars, key=chars.get)]


class Day14(unittest.TestCase):
    def test_dict(self):
        rules = ["CH -> B", "HH -> N", "CB -> H", "NH -> C",
                 "HB -> C", "HC -> B", "HN -> C", "NN -> C",
                 "BH -> H", "NC -> B", "NB -> B", "BN -> B",
                 "BB -> N", "BC -> B", "CC -> N", "CN -> C"]
        polymer = Polymer("NNCB", rules)
        self.assertEqual({"NN": 1, "NC": 1, "CB": 1}, polymer.template)

    def test_one_step(self):
        rules = ["CH -> B", "HH -> N", "CB -> H", "NH -> C",
                 "HB -> C", "HC -> B", "HN -> C", "NN -> C",
                 "BH -> H", "NC -> B", "NB -> B", "BN -> B",
                 "BB -> N", "BC -> B", "CC -> N", "CN -> C"]
        polymer = Polymer("NNCB", rules)
        polymer.step()
        self.assertEqual({"NC": 1, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1}, polymer.template)

    def test_two_steps(self):
        rules = ["CH -> B", "HH -> N", "CB -> H", "NH -> C",
                 "HB -> C", "HC -> B", "HN -> C", "NN -> C",
                 "BH -> H", "NC -> B", "NB -> B", "BN -> B",
                 "BB -> N", "BC -> B", "CC -> N", "CN -> C"]
        polymer = Polymer("NNCB", rules)
        polymer.step(2)
        self.assertEqual({"NB": 2, "BC": 2, "CC": 1, "CN": 1, "BB": 2, "CB": 2, "BH": 1, "HC": 1}, polymer.template)

    def test_example(self):
        rules = ["CH -> B", "HH -> N", "CB -> H", "NH -> C",
                 "HB -> C", "HC -> B", "HN -> C", "NN -> C",
                 "BH -> H", "NC -> B", "NB -> B", "BN -> B",
                 "BB -> N", "BC -> B", "CC -> N", "CN -> C"]
        polymer = Polymer("NNCB", rules)
        polymer.step(10)
        least, most = polymer.get_least_and_most_diff()
        print(least, most)
        self.assertEqual(1588, most - least)

    def test_input_1(self):
        data = read_input_str("input_day_14.txt")
        polymer = Polymer(data[0], data[2:])
        polymer.step(10)

        least, most = polymer.get_least_and_most_diff()
        self.assertEqual(3306, most - least)

    def test_input_2(self):
        data = read_input_str("input_day_14.txt")
        polymer = Polymer(data[0], data[2:])
        polymer.step(40)

        least, most = polymer.get_least_and_most_diff()
        self.assertEqual(0, most - least)
