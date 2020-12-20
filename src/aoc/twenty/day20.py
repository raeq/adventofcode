import dataclasses
import typing
from pprint import pprint
from collections import defaultdict


@dataclasses.dataclass
class Tile:
    name: str
    raw: str = dataclasses.field(repr=False)
    rows: typing.List = dataclasses.field(default_factory=list, repr=False)
    edges: typing.Set = dataclasses.field(default_factory=list, repr=True)

    def __init__(self, raw_data: str = ""):

        if raw_data:
            self.raw = raw_data
            self.rows = raw_data.strip().split('\n')[1:]
            self.name = raw_data.strip().split('\n')[0]
            self.edges = self._fill_edges()

    @staticmethod
    def _translate_edge(edge: str) -> int:
        retVal: int = 0
        try:
            retVal = int(edge.translate(str.maketrans(".#", "01")), 2)
        except ValueError as e:
            raise
        finally:
            return retVal

    def _fill_edges(self) -> set:
        edges: set = set()
        max = len(self.rows) - 1

        edges.add(self._translate_edge(self.rows[0]))
        edges.add(self._translate_edge(self.rows[max]))

        left: str = ""
        right: str = ""
        for r in self.rows:
            left += r[0]
            right += r[max]

        edges.add(self._translate_edge(left))
        edges.add(self._translate_edge(right))

        return edges

    @staticmethod
    def _flip_horizontal(rows) -> list:
        matrix: list = []
        for r in rows:
            matrix.append(r[::-1])
        return matrix

    @staticmethod
    def _flip_vertical(rows) -> list:
        matrix: list = []
        for r in rows[::-1]:
            matrix.append(r)
        return matrix

    def mirror(self):

        matrix: list = self._flip_vertical(self._flip_horizontal(self.rows))

        t = Tile()
        t.raw = self.raw
        t.name = self.name
        t.rows = matrix
        t.edges = t._fill_edges()
        return t


def load_file(file_name: str) -> str:
    with open(file_name, 'r') as fd:
        return fd.read()


def main():
    tiles_raw = load_file("day20.txt").split("\n\n")
    all_tiles: list = []
    tile_dict: defaultdict = defaultdict(set)

    for t in tiles_raw:
        tile1: Tile = Tile(t)
        all_tiles.append(tile1)
        tile2: Tile = tile1.mirror()
        all_tiles.append(tile2)
        tile_dict[tile1.name] = tile_dict[tile1.name].union(tile1.edges)
        tile_dict[tile2.name] = tile_dict[tile2.name].union(tile2.edges)

    edge_dict: defaultdict = defaultdict(set)

    for t in all_tiles:
        for e in t.edges:
            edge_dict[e].add(t.name)

    subset: list =[]
    for y in edge_dict.values():
        if len(y) < 2:
            subset.append(y)

    pprint(subset)

    # print(f"Part one solution: {valid_messages(rules, messages):>5}")
    # print(f"Part two solution: {valid_messages(rules, messages, '2'):>5}")


if __name__ == '__main__':
    main()
