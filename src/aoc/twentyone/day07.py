from math import floor, ceil
from statistics import mean, median


def sum_c(pop: list[int], centroid: int) -> int:
    def gauss_sum(n: int) -> int:
        return (n * (n + 1)) // 2

    return int(sum([gauss_sum(abs(x - centroid)) for x in pop]))


def sum_d(pop: list[int], centroid: int) -> int:
    return int(sum([abs(x - centroid) for x in pop]))


def get_data(fn) -> list:
    print(fn)
    with open(fn) as f:
        file_contents = f.read().rstrip()
        return list(map(int, file_contents.split(',')))


if __name__ == '__main__':
    file_data = get_data("day07.txt")

    print(f"Day 7 Part 1: {sum_d(file_data, (median(file_data)))}")

    # floor or ceil of mean?
    m = mean(file_data)
    fl = sum_c(file_data, floor(m))
    cl = sum_c(file_data, ceil(m))

    print(f"Day 7 Part 2: {fl if fl < cl else cl}")
