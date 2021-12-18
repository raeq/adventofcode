from itertools import product

import networkx as nx


def parse_raw():
    grid = int_grid(open("day15.txt").read())

    G = nx.DiGraph()
    for i, j in product(range(500), repeat=2):
        weight = grid[i % 100, j % 100] + i // 100 + j // 100

        for u, v in DELTAS_4:
            G.add_edge((i + u, j + v), (i, j), weight=weight % 9 or weight)

    return G


DELTAS_4 = (0, 1), (0, -1), (1, 0), (-1, 0)
DELTAS_5 = DELTAS_4 + ((0, 0),)
DELTAS_8 = DELTAS_4 + ((1, 1), (-1, -1), (1, -1), (-1, 1))
DELTAS_9 = DELTAS_8 + ((0, 0),)


def int_grid(raw, np=True, separator=""):
    """
    Parse a grid of ints into a 2d list or numpy array (if np==True).
    """
    array = [
        [int(i) for i in (line.split(separator) if separator else line)]
        for line in raw.splitlines()
    ]

    if np:
        import numpy as np

        return np.array(array)
    return array


def part_one(CAVE):
    return nx.dijkstra_path_length(CAVE, (0, 0), (99, 99))


def part_two(CAVE):
    return nx.dijkstra_path_length(CAVE, (0, 0), (499, 499))


if __name__ == '__main__':
    parsed = parse_raw()

    print(part_one(parsed))
    print(part_two(parsed))
