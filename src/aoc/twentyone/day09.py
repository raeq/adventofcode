from aoc.utils.matrix import Matrix



def get_data(fn) -> list:
    raw_data = []

    with open(fn) as f:
        for line in f:
            raw_data.append([int(x) for x in line.rstrip()])
    return raw_data


def part1(data: list = None) -> int:
    risk_level: int = 0
    m: Matrix = Matrix(data)

    for c in m.trenches():
        risk_level += c.value + 1

    return risk_level


if __name__ == "__main__":
    numbers = get_data("day09.txt")
    print(f"Day 9 Part1 = {part1(numbers)}")
