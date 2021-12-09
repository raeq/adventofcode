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

    print(f"Matrix: {rows} rows and {cols} columns")

    for row_idx, row in enumerate(data):
        for col_idx, col in enumerate(row):
            above_idx = max(0, row_idx - 1)
            below_idx = min(rows - 1, row_idx + 1)

            left_idx = max(0, col_idx - 1)
            right_idx = min(cols - 1, col_idx + 1)

            print(f"cell ({row_idx},{col_idx}) = {col}", end=" ")
            print(f"- a:{above_idx} b:{below_idx} l:{left_idx} r:{right_idx}", end=" ")
            print(f"left = ({row_idx},{left_idx}){data[row_idx][left_idx]}  - ", end=" ")
            print(f"right = ({row_idx},{right_idx}){data[row_idx][right_idx]} ", end=" ")
            print(f"above = ({above_idx},{col_idx}){data[above_idx][col_idx]} ", end=" ")
            print(f"below = ({below_idx},{col_idx}){data[below_idx][col_idx]} ")

    return minrow


if __name__ == "__main__":
    numbers = get_data("day09.txt")
    print(numbers)

    print(part1((numbers)))
