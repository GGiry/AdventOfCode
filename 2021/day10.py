import queue
import unittest
from utils import read_input_str


def is_opening(char):
    return char in ["(", "[", "{", "<"]


def is_correct_chung(open_chunk, close_chunk):
    if open_chunk == "(" and close_chunk == ")":
        return True
    if open_chunk == "[" and close_chunk == "]":
        return True
    if open_chunk == "{" and close_chunk == "}":
        return True
    if open_chunk == "<" and close_chunk == ">":
        return True
    return False


def get_corrupted(line):
    lifo = queue.LifoQueue()
    for char in line:
        if is_opening(char):
            lifo.put(char)
        else:
            last_open = lifo.get()
            if not is_correct_chung(last_open, char):
                return char
    return ""


def to_score(end_chunk):
    if end_chunk is None:
        return 0
    if end_chunk == ")":
        return 3
    if end_chunk == "]":
        return 57
    if end_chunk == "}":
        return 1197
    if end_chunk == ">":
        return 25137


def get_scores(lines):
    result = 0
    for line in lines:
        corrupted = get_corrupted(line)
        if corrupted:
            result += to_score(corrupted)

    return result


def get_incomplete_lines(lines):
    incomplete_lines = []
    for line in lines:
        if "" == get_corrupted(line):
            incomplete_lines.append(line)
    return incomplete_lines


def closing(c):
    if c == "(":
        return ")"
    if c == "[":
        return "]"
    if c == "{":
        return "}"
    if c == "<":
        return ">"


def complete(line):
    lifo = queue.LifoQueue()
    for char in line:
        if is_opening(char):
            lifo.put(char)
        else:
            lifo.get()

    result = ""
    while not lifo.empty():
        c = lifo.get()
        result += closing(c)
    return result


def score(end_chunk):
    if end_chunk is None:
        return 0
    if end_chunk == ")":
        return 1
    if end_chunk == "]":
        return 2
    if end_chunk == "}":
        return 3
    if end_chunk == ">":
        return 4


def get_complete_score(to_score):
    result = 0
    for char in to_score:
        result = result * 5 + score(char)
    return result


def get_incomplete_score(incomplete_lines):
    scores = []
    for line in incomplete_lines:
        scores.append(get_complete_score(complete(line)))

    scores.sort()
    return scores[int(len(scores) / 2)]


class Day10(unittest.TestCase):

    def test_get_score_1(self):
        line = "{([(<{}[<>[]}>{[]{[(<()>"
        self.assertEqual("}", get_corrupted(line))

    def test_get_score_2(self):
        line = "[[<[([]))<([[{}[[()]]]"
        self.assertEqual(")", get_corrupted(line))

    def test_get_score_3(self):
        line = "[{[{({}]{}}([{[{{{}}([]"
        self.assertEqual("]", get_corrupted(line))

    def test_get_score_4(self):
        line = "[<(<(<(<{}))><([]([]()"
        self.assertEqual(")", get_corrupted(line))

    def test_get_score_5(self):
        line = "<{([([[(<>()){}]>(<<{{"
        self.assertEqual(">", get_corrupted(line))

    def test_example_1(self):
        navigation = read_input_str("input_day_10_example.txt")
        self.assertEqual(26397, get_scores(navigation))

    def test_input(self):
        navigation = read_input_str("input_day_10.txt")
        self.assertEqual(339411, get_scores(navigation))

    def test_complete(self):
        line = "[({(<(())[]>[[{[]{<()<>>"
        completion = complete(line)
        self.assertEqual("}}]])})]", completion)
        self.assertEqual(288957, get_complete_score(completion))

    def test_example_2(self):
        navigation = read_input_str("input_day_10_example.txt")
        incomplete_lines = get_incomplete_lines(navigation)
        self.assertEqual(288957, get_incomplete_score(incomplete_lines))

    def test_input2(self):
        navigation = read_input_str("input_day_10.txt")
        incomplete_lines = get_incomplete_lines(navigation)
        self.assertEqual(2289754624, get_incomplete_score(incomplete_lines))
