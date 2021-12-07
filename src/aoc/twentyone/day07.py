def get_mean(pop: list[int]) -> int:
    return round(sum(pop) / len(pop))


def get_data(fn) -> list:
    print(fn)
    with open(fn) as f:
        file_contents = f.read().rstrip()
        return list(map(int, file_contents.split(',')))


def part1(data: list[int]) -> int:
    ...


if __name__ == '__main__':
    file_data = get_data("day07.txt")
    part1(file_data)
    print(get_mean(file_data))
