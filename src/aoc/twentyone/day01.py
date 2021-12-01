import more_itertools


def get_data(filename: str) -> list:
    return_list: list = []

    with open(filename, 'r') as f:
        for line in f:
            return_list.append(int(line.rstrip('\n')))
    return return_list


def make_couples(singles: list) -> list:
    return zip(singles, singles[1:])


def count_increases(couples: list) -> int:
    return sum(next > prev for prev, next in couples)


if __name__ == "__main__":
    depths = get_data("day01.txt")

    depths_couples = make_couples(depths)
    num_increases = count_increases(depths_couples)
    print(f'Day 1 Star 1 answer: {num_increases}')

    window_length = 3
    window_sum = [sum(triple) for triple in more_itertools.triplewise(depths)]

    window_sums_couples = make_couples(window_sum)
    num_increases = count_increases(window_sums_couples)
    print(f'Day 1 Star 2 answer: {num_increases}')
