import itertools
from collections import namedtuple
from statistics import mean, mode, median, stdev


class Matrix:
    fields = ('x', 'y', 'value')
    Point = namedtuple('Point', fields, defaults=(None,) * len(fields))


    class Row:
        _data_points: list
        _row_idx: int

        def __init__(self, row: list[int], row_idx: int = 0):
            self._data_points = []
            self._row_idx = row_idx

            if row_idx < 0:
                raise ValueError(f"Can't have negative rows like {row_idx}")

            for col_idx, val in enumerate(row):
                p: Matrix.Point = Matrix.Point(x=row_idx, y=col_idx, value=val)
                self._data_points.append(p)

        def __getitem__(self, item):
            return self._data_points[item]

        @property
        def row_idx(self) -> int:
            return self._row_idx

        @property
        def data_points(self) -> list[int]:
            return [p.value for p in self._data_points]

        @property
        def unique_data_points(self) -> set[int]:
            return set(self.data_points)

        @property
        def mean(self):
            return mean(self.data_points)

        @property
        def median(self):
            return median(self.data_points)

        @property
        def mode(self):
            return mode(self.data_points)

        @property
        def stdev(self):
            return stdev(self.data_points)

        @property
        def sum(self):
            return sum(self.data_points)

        @property
        def min(self):
            return min(self.data_points)

        @property
        def max(self):
            return max(self.data_points)

        @property
        def short_description(self) -> str:
            return f"Row {self.row_idx} has {len(self._data_points)} columns " \
                   f"sum: {self.sum} " \
                   f"min: {self.min} " \
                   f"max: {self.max} " \
                   f"mean: {self.mean} " \
                   f"median: {self.median} " \
                   f"mode: {self.mode} " \
                   f"stdev: {self.stdev:.2f} "

        def __repr__(self):
            return f'{self.__class__.__name__}({self._data_points})'

        def __str__(self):
            return f','.join([f"({x},{y}={v})" for x, y, v in self._data_points])


    data: list[list[int]]
    rows: list[Row]
    _data_points: list[int]

    def __init__(self, matrix: list[list[int]] = None):

        self.data = matrix
        self._data_points = list(itertools.chain(*self.data))

        self.rows = []
        for idx, row in enumerate(matrix):
            self.rows.append(self.Row(row, row_idx=idx))

    @property
    def row_count(self) -> int:
        return len(self.data)

    @property
    def col_count(self) -> int:
        return len(self.data[0])

    @property
    def transposed(self) -> list[list[int]]:
        return [list(i) for i in zip(*self.data)]

    @property
    def data_points(self) -> list[int]:
        return self._data_points

    @property
    def unique_data_points(self) -> set[int]:
        return set(self.data_points)

    @property
    def mean(self):
        return mean(self.data_points)

    @property
    def median(self):
        return median(self.data_points)

    @property
    def mode(self):
        return mode(self.data_points)

    @property
    def stdev(self):
        return stdev(self.data_points)

    @property
    def sum(self):
        return sum(self.data_points)

    @property
    def min(self):
        return min(self.data_points)

    @property
    def max(self):
        return max(self.data_points)

    @property
    def short_description(self) -> str:

        return f"Matrix has: {self.row_count} rows and {self.col_count} columns, " \
               f"sum: {self.sum}, " \
               f"min: {self.min}, " \
               f"max: {self.max}, " \
               f"mean: {self.mean}, " \
               f"median: {self.median}, " \
               f"mode: {self.mode}, " \
               f"stdev: {self.stdev:.2f} "

    @property
    def long_description(self):

        msg = self.short_description + "\n"
        for idx, row in enumerate(self.rows):
            msg = msg + f"Row: {idx}, " \
                        f"sum: {row.sum}, " \
                        f"min: {row.min}, " \
                        f"max: {row.max}, " \
                        f"mean: {row.mean}, " \
                        f"median: {row.median}, " \
                        f"mode: {row.mode}, " \
                        f"stdev: {row.stdev:.2f}, " \
                        f"unique value count: {len(row.unique_data_points)}\n"

        return msg

    def walk_path(self, start: Point, end: Point):
        """
        Bresenham algorithm
        Yield integer coordinates on the line from (x0, y0) to (x1, y1).
        Input coordinates should be integers.
        The result will contain both the start and the end point.
        See en.wikipedia.org/wiki/Bresenham's_line_algorithm
        """
        dx = abs(end.x - start.x)
        dy = abs(end.y - start.y)
        x0 = start.x
        y0 = start.y

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
            myx = x0 + x * xx + y * yx
            myy = y0 + x * xy + y * yy

            yield self.rows[myx][myy]
            if d >= 0:
                y += 1
                d -= 2 * dx
            d += 2 * dy

    def display(self):

        for row_idx, row in enumerate(self.rows):
            print(row)

    def neighbours(self, loc: Point, include_diagonals: bool = False, distance: int = 1):

        distance = max(min(distance, self.row_count), min(distance, self.col_count))
        for row in range(-distance, distance + 1):
            for col in range(-distance, distance + 1):
                if row == 0 and col == 0:  # this is the center, it is not a neighbour
                    continue

                if not include_diagonals:
                    if row != 0 and col != 0:
                        continue

                tx = loc.x + row
                ty = col + loc.y

                if tx >= 0 and ty >= 0:  # not out of bounds
                    if tx < self.row_count and ty < self.col_count:  # not out of bounds
                        yield self.rows[tx][ty]

    def cell_value(self, x: int, y: int) -> [int, None]:
        if (x < 0 or x >= self.row_count) or (y < 0 or y >= self.col_count):
            return None
        try:
            return self.rows[x][y].value
        except IndexError as e:
            print(e, "loc= ", x, y)
            raise IndexError(e)

    def all_cells(self):
        for r in self.rows:
            for c in r._data_points:
                yield c

    def trenches(self, include_diagonals: bool = False):
        """The trenches in the matrix are cells with a value lower than any neighbour"""

        for c in self.all_cells():
            for n in self.neighbours(c, include_diagonals):
                if c.value >= n.value:
                    break
            else:
                yield c

    def peaks(self, include_diagonals: bool = False):
        """The peaks in the matrix are cells with a value higher than any neighbour"""

        for c in self.all_cells():
            for n in self.neighbours(c, include_diagonals):
                if c.value <= n.value:
                    break
            else:
                yield c

    def plateaus(self, include_diagonals: bool = False):
        """The plateaus in the matrix are cells with a value equal to all neighbours"""

        for c in self.all_cells():
            for n in self.neighbours(c, include_diagonals):
                if c.value != n.value:
                    break
            else:
                yield c


if __name__ == '__main__':

    data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    raw_data: list[list[int]] = []

    for line in data.split("\n"):
        raw_data.append([int(x) for x in line.rstrip()])

    m: Matrix = Matrix(matrix=raw_data)

    print(m.short_description)
    print(m.long_description)

    m.display()
    print("trenches", list(m.trenches(include_diagonals=True)))
    print("peaks", list(m.peaks(include_diagonals=True)))
    print("plateaus", list(m.plateaus()))
    print("path", list(m.walk_path(start=Matrix.Point(x=0, y=0),
                                   end=Matrix.Point(x=3, y=8))))
    print("neighbours of 2,4", list(m.neighbours(
        loc=Matrix.Point(x=2, y=4), include_diagonals=False, distance=234543524352
    )))
