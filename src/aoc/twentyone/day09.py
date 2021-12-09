import statistics
from itertools import chain


def get_data(fn) -> list:
    raw_data = []

    with open(fn) as f:
        for line in f:
            raw_data.append([int(x) for x in line.rstrip()])
    return raw_data


def transpose_rows_to_columns(rows) -> list:
    return [list(i) for i in zip(*rows)]


def describe_matrix(data: list = None):
    rows = len(data)
    cols = len(data[0])

    for row in data:
        print(row)
    print()

    all_values = list(chain(*data))

    print(f"Matrix has: {rows} rows and {cols} columns "
          f"sum: {sum(all_values)} "
          f"min: {min(all_values)} "
          f"max: {max(all_values)} "
          f"mean: {statistics.mean(all_values)} "
          f"median: {statistics.median(all_values)} "
          f"mode: {statistics.mode(all_values)} "
          f"stdev: {statistics.stdev(all_values):.2f} ", end="\n\n")

    for row_idx, row in enumerate(data):
        print(f"Row {row_idx}: "
              f"sum: {sum(row)} "
              f"min: {min(row)} "
              f"max: {max(row)} "
              f"mean: {statistics.mean(row)} "
              f"median: {statistics.median(row)} "
              f"mode: {statistics.mode(row)} "
              f"stdev: {statistics.stdev(row):.2f} ")

        for col_idx, col in enumerate(row):
            above_idx = max(0, row_idx - 1)
            below_idx = min(rows - 1, row_idx + 1)

            left_idx = max(0, col_idx - 1)
            right_idx = min(cols - 1, col_idx + 1)

            above_left = ""
            above_right = ""

            below_left = ""
            below_right = ""

            print(f"cell \33({row_idx},{col_idx}) = {col}", end=" ")
            print(f"- a:{above_idx} b:{below_idx} l:{left_idx} r:{right_idx}", end=" ")
            print(f"left = ({row_idx},{left_idx}){data[row_idx][left_idx]}  - ", end=" ")
            print(f"right = ({row_idx},{right_idx}){data[row_idx][right_idx]} ", end=" ")
            print(f"above = ({above_idx},{col_idx}){data[above_idx][col_idx]} ", end=" ")
            print(f"below = ({below_idx},{col_idx}){data[below_idx][col_idx]} ")

        print(end="\n")


def part1(data: list = None) -> int:
    minrow = 0
    rows = len(data)
    cols = len(data[0])

    describe_matrix(data)

    for row_idx, row in enumerate(data):
        for col_idx, col in enumerate(row):
            above_idx = max(0, row_idx - 1)
            below_idx = min(rows - 1, row_idx + 1)

            left_idx = max(0, col_idx - 1)
            right_idx = min(cols - 1, col_idx + 1)

    return minrow


if __name__ == "__main__":
    numbers = get_data("day09.txt")

    print(part1((numbers)))
