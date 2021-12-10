import itertools
from collections import namedtuple
from statistics import mean, mode, median, stdev


class Matrix():
    fields = ('x', 'y', 'value')
    Point = namedtuple('Point', fields, defaults=(None,) * len(fields))


    class Row:
        _data_points: list[int]

        def __init__(self, row: list[int]):
            self._data_points = row

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
            return f"Matrix has: {self.row_count} rows and {self.col_count} columns " \
                   f"sum: {self.sum} " \
                   f"min: {self.min} " \
                   f"max: {self.max} " \
                   f"mean: {self.mean} " \
                   f"median: {self.median} " \
                   f"mode: {self.mode} " \
                   f"stdev: {self.stdev:.2f} "


    data: list[list[int]]
    rows: list[Row]
    _data_points: list[int]

    def __init__(self, matrix: list[list[int]] = None):

        self.data = matrix
        self._data_points = list(itertools.chain(*self.data))

        self.rows = []
        for row in matrix:
            self.rows.append(self.Row(row))

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

        msg = "\n"
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

        msg = self.short_description + msg
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

            yield Matrix.Point(x=myx, y=myy, value=self.cell_value(self.Point(x=myx, y=myy)))
            if d >= 0:
                y += 1
                d -= 2 * dx
            d += 2 * dy

    def display(self):

        for row_idx, row in enumerate(self.data):
            for col_idx, col in enumerate(row):
                above_idx = row_idx - 1
                below_idx = row_idx + 1

                left_idx = col_idx - 1
                right_idx = col_idx + 1

                above_left = ""
                above_right = ""

                below_left = ""
                below_right = ""

                print(f"cell \33({row_idx},{col_idx}) = {col}", end=" ")
                print(f"- a:{above_idx} b:{below_idx} l:{left_idx} r:{right_idx}", end=" ")
                print(f"left = ({row_idx},{left_idx}){self.cell_value(self.Point(x=row_idx, y=left_idx))}  - ",
                      end=" ")
                print(f"right = ({row_idx},{right_idx}){self.cell_value(self.Point(x=row_idx, y=right_idx))} ",
                      end=" ")
                print(f"above = ({above_idx},{col_idx}){self.cell_value(self.Point(x=above_idx, y=col_idx))} ",
                      end=" ")
                print(f"below = ({below_idx},{col_idx}),{self.cell_value(self.Point(x=below_idx, y=col_idx))} ")

            print(end="\n")

    def neighbours(self, loc: Point, distance: int = 1):

        for row in range(-distance, distance + 1):
            for col in range(-distance, distance + 1):
                if row == 0 and col == 0:  # this is the center, it is not a neighbour
                    continue
                else:
                    yield self.Point(x=loc.x + row, y=col + loc.y,
                                     value=self.cell_value(self.Point(x=loc.x, y=loc.y)))

    def cell_value(self, loc: Point) -> [int, None]:
        if (loc.x < 0 or loc.x >= self.row_count) or (loc.y < 0 or loc.y >= self.col_count):
            return None

        try:
            return self.data[loc.x][loc.y]
        except IndexError as e:
            print(e, "loc= ", loc)
            raise IndexError(e)


def get_data(fn) -> list:
    raw_data = []

    with open(fn) as f:
        for line in f:
            raw_data.append([int(x) for x in line.rstrip()])
    return raw_data


def part1(data: list = None) -> int:
    minrow = 0
    rows = len(data)
    cols = len(data[0])

    m: Matrix = Matrix(data)
    print(m.long_description)
    m.display()
    print(list(m.walk_path(Matrix.Point(x=0, y=0), Matrix.Point(x=2, y=4))))
    print(list(m.neighbours(m.Point(x=1, y=2))))

    return minrow


if __name__ == "__main__":
    numbers = get_data("day09.txt")

    print(part1((numbers)))
