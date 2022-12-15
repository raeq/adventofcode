import regex as re
from more_itertools import chunked

from aoc.utils.matrix import Matrix, Point

EMPTY = 0
SENSOR = 1
BEACON = 2


def get_int_pairs(input: str) -> tuple[Point, Point]:
    matches = re.findall(r"[\d]+", input, re.IGNORECASE | re.DOTALL)
    for val0, val1, val2, val3 in chunked(matches, 4):
        return Point(int(val0), int(val1), SENSOR), \
               Point(int(val2), int(val3), BEACON)


m: Matrix = Matrix([])

with open("day15.txt") as f:
    for line in f.readlines():
        x, y = get_int_pairs(line)
        print(f'{x=}, {y=}')
        print(m.manhattan_distance(x, y), end='\n\n')
