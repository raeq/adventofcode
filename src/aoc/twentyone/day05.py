from collections import defaultdict
from typing import NamedTuple
from pprint import pprint as pp


class Point(NamedTuple):
    x: int
    y: int


class Segment(NamedTuple):
    start: Point
    finish: Point

    @property
    def is_horizontal(self) -> bool:
        return self.start.x == self.finish.x

    @property
    def is_vertical(self) -> bool:
        return self.start.y == self.finish.y

    @property
    def is_straight(self) -> bool:
        return self.is_horizontal or self.is_vertical

    @property
    def x_distance(self) -> int:
        return self.finish.x - self.start.x

    @property
    def y_distance(self):
        return self.finish.y - self.start.y


def get_data(fn):
    cordinate_pairs: list = []

    with open(fn) as f:
        for line in f:
            line = line.strip().split(" -> ")
            for idx, item in enumerate(line):
                line[idx] = tuple(map(int, item.split(',')))
                line[idx] = Point(x=line[idx][0], y=line[idx][1])
            cordinate_pairs.append(Segment(start=line[0], finish=line[1]))

    return cordinate_pairs


def calculate(segment_list: list):
    G1: dict = defaultdict(int)
    G2: dict = defaultdict(int)
    s: Segment

    for idx, s in enumerate(segments):

        for i in range(1 + max(abs(s.x_distance), abs(s.y_distance))):
            x = s.start.x + (1 if s.x_distance > 0 else (-1 if s.x_distance < 0 else 0)) * i
            y = s.start.y + (1 if s.y_distance > 0 else (-1 if s.y_distance < 0 else 0)) * i
            if s.is_straight:
                G1[(x, y)] += 1
            G2[(x, y)] += 1

    print(len([k for k in G1 if G1[k] > 1]))
    print(len([k for k in G2 if G2[k] > 1]))


if __name__ == '__main__':
    segments: list = get_data("day05.txt")
    calculate(segments)
