def get_data(fn):
    data: list = []
    with open(fn) as f:
        for line in f:
            data.append(line.rstrip())
    return data


def transpose_rows_to_columns(rows) -> list:
    return [list(i) for i in zip(*rows)]


def is_col_mostly_one(column, rows) -> bool:
    return column.count('1') * 2 >= rows


def part_1(input_data) -> int:
    rows, cols = len(input_data), len(input_data[0])
    transposition = transpose_rows_to_columns(input_data)

    powers_two = [pow(2, x) for x in range(cols - 1, -1, -1)]
    gamma, epsilon = 0, 0

    for idx, column in enumerate(transposition):
        match is_col_mostly_one(column, rows):
            case True:
                gamma += powers_two[idx]
            case _:
                epsilon += powers_two[idx]

    return gamma * epsilon


def main():
    data = get_data("day03.txt")
    print(f'Day 3 Part 1: {part_1(data)}')


if __name__ == "__main__":
    main()
