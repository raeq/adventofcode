def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        d = fd.read()
    return list(map(int, d.split(',')))


def van_eck(data, nth):
    memory = {}

    it = iter(data)
    last = next(it)

    for i, n in enumerate(it, start=1):
        memory[last], last = i, n

    for i in range(len(data), nth):
        memory[last], last = i, i - memory[last] if last in memory else 0

    return last


def part_one(data: list):
    return van_eck(data, 2020)


def part_two(data: list):
    return van_eck(data, 30000000)


if __name__ == '__main__':
    data = load_file("day15.txt")
    print(f"Part one answer: {part_one(data)}")
    print(f"Part two answer: {part_two(data)}")
