from typing import List


class Radar:

    @staticmethod
    def count_increase(depths):
        result = 0
        previous = None
        for depth in depths:
            if previous and previous < depth:
                result += 1
            previous = depth
        return result

    @staticmethod
    def window_total(depths, index):
        return sum(depths[index - 1: index + 2])

    @staticmethod
    def count_increase_sliding(depths):
        result = 0

        for i in range(2, len(depths) - 1):
            window_a = Radar.window_total(depths, i - 1)
            window_b = Radar.window_total(depths, i)

            if window_a < window_b:
                result += 1

        return result


class Submarine:
    def __init__(self, radar=Radar()):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0
        self.radar = radar

    def move(self, moves: List[str]):
        for move in moves:
            command, units = move.split()
            if command == "forward":
                self.horizontal += int(units)
            elif command == "down":
                self.depth += int(units)
            elif command == "up":
                self.depth -= int(units)
            else:
                print(f"Command incorrect: {move}")

    def move_aim(self, moves: List[str]):
        for move in moves:
            command, units = move.split()
            if command == "forward":
                self.horizontal += int(units)
                self.depth += self.aim * int(units)
            elif command == "down":
                self.aim += int(units)
            elif command == "up":
                self.aim -= int(units)
            else:
                print(f"Command incorrect: {move}")

    def get_position(self):
        return self.depth * self.horizontal
