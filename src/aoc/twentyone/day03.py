def get_data(fn):
    data: list = []
    with open(fn) as f:
        for line in f:
            data.append(line.rstrip())
    return data


def part_1(input_data):
    rows, cols = len(input_data), len(input_data[0])
    transposition = list(zip(*input_data))
    Trues = [x * 2 >= rows for x in [y.count('1') for y in transposition]]

    powers_two = [pow(2, x) for x in range(cols - 1, -1, -1)]
    gamma, epsilon = 0, 0
    for idx, value in enumerate(Trues):
        if value:
            gamma += powers_two[idx]
        else:
            epsilon += powers_two[idx]

    return gamma * epsilon


def main():
    data = get_data("day03.txt")
    print(f'Day 3 Part 1: {part_1(data)}')


if __name__ == "__main__":
    main()
