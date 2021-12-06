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


def add_new_generation(fish_counts_yesterday: Counter) -> dict:
    fish_counts_new_day: dict = {}

    fish_counts_new_day[0] = fish_counts_yesterday[1]
    fish_counts_new_day[1] = fish_counts_yesterday[2]
    fish_counts_new_day[2] = fish_counts_yesterday[3]
    fish_counts_new_day[3] = fish_counts_yesterday[4]
    fish_counts_new_day[4] = fish_counts_yesterday[5]
    fish_counts_new_day[5] = fish_counts_yesterday[6]
    fish_counts_new_day[6] = fish_counts_yesterday[0] + fish_counts_yesterday[7]
    fish_counts_new_day[7] = fish_counts_yesterday[8]
    fish_counts_new_day[8] = fish_counts_yesterday[0]

    return fish_counts_yesterday


if __name__ == '__main__':
    raw_data = get_data("day06.txt")

    # answer, c = calculate(data=raw_data, cycles=80)
    # print(f"Day 6 Part 1: {answer}")

    answer, c = calculate(data=raw_data, cycles=10_000_000)
    print(f"Day 6 Part 2: {answer}")
