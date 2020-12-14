from functools import lru_cache


def parse_raw(file_name: str) -> list:
    with open(file_name, "r") as fd:
        data = [int(_.rstrip('\n')) for _ in fd.readlines()]

    data += 0, max(data) + 3
    return sorted(data)


from collections import Counter
from math import prod
from more_itertools import difference


def part_one(data: list) -> int:
    return prod(v for k, v in dict(Counter(difference(data[1:]))).items())


@lru_cache(maxsize=2)
def part_two(current: int = 0) -> int:
    if current != len(data) - 1:
        return sum(part_two(current + next_val) for
                   next_val in range(1, min(4, len(data) - current))
                   if data[next_val + current] - data[current] <= 3)
    return 1


data: list

if __name__ == "__main__":
    data = parse_raw("day10.txt")
    print(f"Part one answer: {part_one(data):>20}")
    print(f"Part two answer: {part_two():>20}")
