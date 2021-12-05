from collections import defaultdict
from typing import NamedTuple


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

    @property
    def walk_path(self):
        """
        Bresenham algorithm
        Yield integer coordinates on the line from (x0, y0) to (x1, y1).
        Input coordinates should be integers.
        The result will contain both the start and the end point.
        See en.wikipedia.org/wiki/Bresenham's_line_algorithm
        """
        dx = self.x_distance
        dy = self.y_distance
        x0 = self.start.x
        y0 = self.start.y

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        d = 2 * dy - dx
        y = 0

        for x in range(dx + 1):
            yield Point(x=x0 + x * xx + y * yx, y=y0 + x * xy + y * yy)
            if d >= 0:
                y += 1
                d -= 2 * dx
            d += 2 * dy


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
    p: Point

    for s in segments:
        if s.is_straight:
            for p in s.walk_path:
                G1[(p.x, p.y)] += 1
                G2[(p.x, p.y)] += 1
        else:
            for p in s.walk_path:
                G2[(p.x, p.y)] += 1

    print(len([k for k in G1 if G1[k] > 1]))
    print(len([k for k in G2 if G2[k] > 1]))


if __name__ == '__main__':
    segments: list = get_data(r"day05.txt")
    calculate(segments)
