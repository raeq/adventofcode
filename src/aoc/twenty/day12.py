from collections import namedtuple as nt
from functools import lru_cache
from pprint import pprint
from more_itertools import difference

Loc: nt = nt('Loc', ['x', 'y', 'd'])
directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

def parse_raw(file_name: str) -> list:
    with open(file_name, "r") as fd:
        data = [_.rstrip('\n') for _ in fd.readlines()]
    return (data)

s = "NESW"


def part_one(lines: list):

    turns = []

    x, y = 0, 0
    f = 1

    for line in lines:
        d = line[0]
        k = int(line[1:])

        if d in directions:
            dx, dy = directions[d]
            x += k * dx
            y += k * dy
        else:
            dc = (k // 90)
            if d == 'L':
                f = (f - dc) % 4
            elif d == 'R':
                f = (f + dc) % 4
            else:
                dx, dy = directions[s[f]]
                x += k * dx
                y += k * dy

        turns.append(Loc(x=x, y=y, d=line))

    pprint(turns)
    return abs(x) + abs(y)


def part_two(lines: list):
    turns: list = []

    x, y = 0, 0

    wx, wy = 10, 1
    f = 1
    for line in lines:
        d = line[0]
        k = int(line[1:])

        if d in directions:
            dx, dy = directions[d]
            wx += k * dx
            wy += k * dy
        else:
            dc = (k // 90)
            dc %= 4
            if d == 'L':
                dc = 4 - dc
            if d in 'LR':
                for _ in range(dc):
                    wx, wy = wy, -wx
            else:
                x += k * wx
                y += k * wy

            turns.append(Loc(x=x, y=y, d=line))

    pprint(turns)
    return abs(x) + abs(y)


if __name__ == "__main__":

    data = parse_raw("day12.txt")
    print(f"Part one answer: {part_one(data)}")
    print(f"Part two answer: {part_two(data)}")
