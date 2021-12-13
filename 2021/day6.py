import unittest
from utils import read_input_str


class School:
    def __init__(self, lanterfish_values):
        self.fish = []
        for value in lanterfish_values:
            self.fish.append(Lanternfish(value, self))

    def simulate_days(self, number_of_days):
        for i in range(number_of_days):
            for fish in self.fish:
                fish.simulate()

    def create_new_fish(self):
        self.fish.append(Lanternfish(9, self))

    def __str__(self):
        result = []
        for fish in self.fish:
            result.append(fish.days_to_go)
        return str(result)


class Lanternfish:
    def __init__(self, days_to_go, school=None):
        self.school = school
        self.days_to_go = days_to_go

    def simulate(self):
        if self.days_to_go > 0:
            self.days_to_go -= 1
        else:
            self.days_to_go = 6
            if self.school:
                self.school.create_new_fish()


class School2:
    def __init__(self, lanterfish_values):
        self.fish = [0 for _ in range(9)]

        for value in lanterfish_values:
            self.fish[value] += 1

    def simulate_days(self, number_of_days):
        for i in range(number_of_days):
            ready_count = self.fish[0]
            for j in range(8):
                self.fish[j] = self.fish[j + 1]

            self.fish[6] += ready_count
            self.fish[8] = ready_count


class Day6(unittest.TestCase):

    def test_lanterfish(self):
        lanternfish = Lanternfish(1)
        self.assertEqual(1, lanternfish.days_to_go)
        lanternfish.simulate()
        self.assertEqual(0, lanternfish.days_to_go)
        lanternfish.simulate()
        self.assertEqual(6, lanternfish.days_to_go)

    def test_simulate_3_days(self):
        lanternfish_school = School([3, 4, 3, 1, 2])
        lanternfish_school.simulate_days(3)
        self.assertEqual(str([0, 1, 0, 5, 6, 7, 8]), str(lanternfish_school))

    def test_example_1(self):
        lanternfish_school = School([3, 4, 3, 1, 2])
        lanternfish_school.simulate_days(18)
        self.assertEqual(str([6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]),
                         str(lanternfish_school))
        self.assertEqual(26, len(lanternfish_school.fish))

    def prepare_input(self, path):
        result = []
        list_str = read_input_str(path)
        numbers_str = list_str[0].split(",")
        for number_str in numbers_str:
            result.append(int(number_str))
        return result

    def test_simulate_3_days_2(self):
        lanternfish_school = School2([3, 4, 3, 1, 2])
        lanternfish_school.simulate_days(3)
        self.assertEqual(len([0, 1, 0, 5, 6, 7, 8]), sum(lanternfish_school.fish))

    def test_input_1(self):
        school = School(self.prepare_input("input_day_6.txt"))
        school.simulate_days(80)
        self.assertEqual(359344, len(school.fish))

    def test_example_1_1(self):
        lanternfish_school = School2([3, 4, 3, 1, 2])
        lanternfish_school.simulate_days(18)
        self.assertEqual(26, sum(lanternfish_school.fish))

    def test_example_1_2(self):
        lanternfish_school = School2([3, 4, 3, 1, 2])
        lanternfish_school.simulate_days(80)
        self.assertEqual(5934, sum(lanternfish_school.fish))

    def test_example_2(self):
        lanternfish_school = School2([3, 4, 3, 1, 2])
        lanternfish_school.simulate_days(256)
        self.assertEqual(26984457539, sum(lanternfish_school.fish))

    def test_input_2(self):
        school = School2(self.prepare_input("input_day_6.txt"))
        school.simulate_days(256)
        self.assertEqual(0, sum(school.fish))
