from typing import List


def read_input_str(path: str) -> List[str]:
    with open(path, encoding='utf-8') as file:
        lines = file.readlines()

    result = []
    for line in lines:
        result.append(line.strip())

    return result


def read_input_int(path: str) -> List[int]:
    lines = read_input_str(path)
    result = []
    for line in lines:
        result.append(int(line))
    return result
