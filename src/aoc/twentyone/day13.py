import re

import numpy as np


def parse_raw(fn: str):
    _points, _instructions = open(fn).read().split("\n\n")

    paper = np.zeros((895, 1311), dtype=bool)
    for x, y in re.findall(r"(\d+),(\d+)", _points):
        paper[int(y), int(x)] = 1

    instructions = re.findall(r"fold along ([xy])=\d+", _instructions)
    return paper, instructions


def fold(paper, axis):
    match axis:
        case "x":
            w = paper.shape[1] >> 1
            return paper[:, :w] | paper[:, -1: w: -1]
        case "y":
            h = paper.shape[0] >> 1
            return paper[:h] | paper[-1: h: -1]


def dot_print(array):
    """
    Pretty print a binary or boolean array.
    """
    for row in array:
        print("".join(" #"[i] for i in row))


def part_one():
    return fold(PAPER, INSTRUCTIONS[0]).sum()


def part_two():
    paper = PAPER
    for instruction in INSTRUCTIONS:
        paper = fold(paper, instruction)

    dot_print(paper)
    return "JRZBLGKH", paper  # after inspection


if __name__ == '__main__':
    PAPER, INSTRUCTIONS = parse_raw(fn="day13.txt")

    print(part_one())
    print(part_two())
