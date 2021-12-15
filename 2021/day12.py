import copy
import unittest
from typing import List


def is_cave_small(from_cave):
    if "end" == from_cave or from_cave == from_cave.upper():
        return False
    return True


class CaveSystem:
    def __init__(self, paths: List[str]):
        self.vertices_count = 0
        self.caves = {}
        self.paths = []
        for path in paths:
            a, b = path.split("-")

            if a not in self.caves:
                self.caves[a] = []
                self.vertices_count += 1
            if b not in self.caves:
                self.caves[b] = []
                self.vertices_count += 1

            self.caves[a].append(b)
            self.caves[b].append(a)

    def __repr__(self):
        return str(self.caves)

    def count_paths(self):
        visited = []
        path = []
        self.count_from_to("start", "end", visited, path, "")
        return len(self.paths)

    def count_from_to(self, from_cave, to_cave, visited, current_path, twice):
        if is_cave_small(from_cave):
            if from_cave == twice:
                twice = ""
            else:
                visited.append(from_cave)

        current_path.append(from_cave)

        if from_cave == to_cave:
            if current_path not in self.paths:
                self.paths.append(copy.deepcopy(current_path))
        else:
            for cave in self.caves[from_cave]:
                if cave not in visited:
                    self.count_from_to(cave, to_cave, visited, current_path, twice)

        current_path.pop()
        if from_cave in visited:
            visited.remove(from_cave)
        return

    def count_paths_twice(self):
        visited = []
        path = []
        for cave in self.caves.keys():
            if cave != "start" and cave != "end" and is_cave_small(cave):
                self.count_from_to("start", "end", visited, path, cave)
        return len(self.paths)


class Day12(unittest.TestCase):
    def test_print(self):
        paths = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
        caves = CaveSystem(paths)
        self.assertEqual(
            "{'start': ['A', 'b'], 'A': ['start', 'c', 'b', 'end'], 'b': ['start', 'A', 'd', 'end'], " +
            "'c': ['A'], 'd': ['b'], 'end': ['A', 'b']}",
            str(caves))

    def test_start_end(self):
        paths = ["start-end"]
        caves = CaveSystem(paths)
        self.assertEqual(1, caves.count_paths())

    def test_start_a_end(self):
        paths = ["start-end", "start-a", "a-end"]
        caves = CaveSystem(paths)
        self.assertEqual(2, caves.count_paths())

    def test_simple(self):
        paths = ["start-a", "start-b", "a-end", "b-end"]
        caves = CaveSystem(paths)
        self.assertEqual(2, caves.count_paths())

    def test_example_1_1(self):
        paths = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
        caves = CaveSystem(paths)
        self.assertEqual(10, caves.count_paths())

    def test_example_1_2(self):
        paths = ["dc-end", "HN-start", "start-kj", "dc-start", "dc-HN", "LN-dc", "HN-end", "kj-sa", "kj-HN", "kj-dc"]
        caves = CaveSystem(paths)
        self.assertEqual(19, caves.count_paths())

    def test_example_1_3(self):
        paths = ["fs-end", "he-DX", "fs-he", "start-DX", "pj-DX", "end-zg", "zg-sl", "zg-pj", "pj-he",
                 "RW-he", "fs-DX", "pj-RW", "zg-RW", "start-pj", "he-WI", "zg-he", "pj-fs", "start-RW"]
        caves = CaveSystem(paths)
        self.assertEqual(226, caves.count_paths())

    def test_input_1(self):
        paths = ["ax-end", "xq-GF", "end-xq", "im-wg", "ax-ie", "start-ws", "ie-ws",
                 "CV-start", "ng-wg", "ng-ie", "GF-ng", "ng-av", "CV-end", "ie-GF",
                 "CV-ie", "im-xq", "start-GF", "GF-ws", "wg-LY", "CV-ws", "im-CV", "CV-wg"]
        caves = CaveSystem(paths)
        self.assertEqual(3576, caves.count_paths())

    def test_example_2_1(self):
        paths = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
        caves = CaveSystem(paths)
        self.assertEqual(36, caves.count_paths_twice())

    def test_example_2_2(self):
        paths = ["dc-end", "HN-start", "start-kj", "dc-start", "dc-HN", "LN-dc", "HN-end", "kj-sa", "kj-HN", "kj-dc"]
        caves = CaveSystem(paths)
        self.assertEqual(103, caves.count_paths_twice())

    def test_example_2_3(self):
        paths = ["fs-end", "he-DX", "fs-he", "start-DX", "pj-DX", "end-zg", "zg-sl", "zg-pj", "pj-he",
                 "RW-he", "fs-DX", "pj-RW", "zg-RW", "start-pj", "he-WI", "zg-he", "pj-fs", "start-RW"]
        caves = CaveSystem(paths)
        self.assertEqual(3509, caves.count_paths_twice())

    def test_input_2(self):
        paths = ["ax-end", "xq-GF", "end-xq", "im-wg", "ax-ie", "start-ws", "ie-ws",
                 "CV-start", "ng-wg", "ng-ie", "GF-ng", "ng-av", "CV-end", "ie-GF",
                 "CV-ie", "im-xq", "start-GF", "GF-ws", "wg-LY", "CV-ws", "im-CV", "CV-wg"]
        caves = CaveSystem(paths)
        self.assertEqual(84271, caves.count_paths_twice())
