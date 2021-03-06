from collections import defaultdict
from itertools import product
from math import prod
import networkx as nx
import numpy as np
from scipy.ndimage import convolve


def borders(tile):
    for i in (0, (..., -1), -1, (..., 0)):
        yield min(tile[i].tobytes(), tile[i][::-1].tobytes())


border_to_tiles = defaultdict(list)  # Build a network of connected tiles from this


def part_one(tiles):
    # Build dict of connections between tiles
    for n, tile in tiles.items():
        for border in borders(tile):
            border_to_tiles[border].append(n)

    return prod(n for n, tile in tiles.items() if sum(len(border_to_tiles[border]) for border in borders(tile)) == 6)


def orientations(tile):
    for _ in range(4):
        tile = np.rot90(tile)
        yield tile
        yield tile.T


def part_two():
    G = nx.Graph(edge for edge in border_to_tiles.values() if len(edge) == 2)

    # Get a corner
    for node in G:
        if len(G[node]) == 2:
            break
    # Orient the corner
    for tile in orientations(tiles[node]):
        if [len(border_to_tiles[border]) for border in borders(tile)] == [1, 2, 2, 1]:
            break

    grid = {}
    grid[0, 0] = node, tile
    # Fill in the rest of the grid by correctly orienting the neighbors
    for y, x in product(range(12), repeat=2):
        node, tile = grid[y, x]
        for neighbor in G[node]:
            for neighbor_tile in orientations(tiles[neighbor]):
                if np.array_equal(tile[-1], neighbor_tile[0]):
                    grid[y + 1, x] = neighbor, neighbor_tile
                    break
                if np.array_equal(tile[:, -1], neighbor_tile[:, 0]):
                    grid[y, x + 1] = neighbor, neighbor_tile
                    break
        G.remove_node(node)

    image = np.block([[grid[y, x][1][1: -1, 1: -1] for x in range(12)] for y in range(12)])
    lochness = np.array([[char == "#" for char in line] for line in
                         "                  #  \n"
                         "#    ##    ##    ### \n"
                         " #  #  #  #  #  #    \n".splitlines()
                         ])
    for lochness in orientations(lochness):
        if count := (convolve(image, lochness, output=int, mode="constant") == lochness.sum()).sum():
            return image.sum() - count * lochness.sum()


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return fd.read()


def parse_raw(raw):
    tiles = {}
    for tile in raw.split("\n\n"):
        it = iter(tile.splitlines())
        number = int(next(it)[5:-1])
        tiles[number] = np.array([[char == "#" for char in line] for line in it])
    return tiles



if __name__ == '__main__':

    raw = load_file("day20.txt")
    tiles = parse_raw(raw)

    print(f"Part one solution: {part_one(tiles):>5}")
    print(f"Part two solution: {part_two():>5}")


