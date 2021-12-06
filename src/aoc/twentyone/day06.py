from collections import Counter
from typing import Tuple


def get_data(fn) -> list:
    with open(fn) as f:
        return list(map(int, f.read().rstrip().split(',')))


def calculate(data: list, cycles=80, counter: Counter = None) -> Tuple[int, Counter]:
    if not counter:
        counter = Counter(data)

    for _ in range(cycles):
        counter = add_new_generation(counter)

    return sum(counter.values()), counter


def add_new_generation(fish_ages_yesterday: Counter) -> dict:
    fish_ages_new_day: dict = {}

    for age in range(6):
        fish_ages_new_day[age] = fish_ages_yesterday[age + 1]
    fish_ages_new_day[6] = fish_ages_yesterday[0] + fish_ages_yesterday[7]
    fish_ages_new_day[7] = fish_ages_yesterday[8]
    fish_ages_new_day[8] = fish_ages_yesterday[0]

    return fish_ages_new_day


if __name__ == '__main__':
    raw_data = get_data("day06.txt")

    answer, c = calculate(data=raw_data, cycles=80)
    print(f"Day 6 Part 1: {answer}")

    answer, c = calculate(data=raw_data, cycles=256 - 80, counter=c)
    print(f"Day 6 Part 2: {answer}")

    # https://en.wikipedia.org/wiki/Leslie_matrix
    import numpy as np


    mat = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int64)

    part1 = np.linalg.matrix_power(mat, 80).sum(axis=0)
    part2 = np.linalg.matrix_power(mat, 256).sum(axis=0)

    print(sum(part1[i] + part2[i] * 1j for i in raw_data))
