from functools import lru_cache
from more_itertools import bucket, difference


def parse_raw(file_name: str) -> list:
    with open(file_name, "r") as fd:
        data = [int(_.rstrip('\n')) for _ in fd.readlines()]

    data += 0, max(data) + 3
    return sorted(data)


#using more_itertools, this is fun!
def part_one(data: []) -> int:
    diffs = list(difference(data[1:]))
    buckets = bucket(diffs, key=lambda x: x)
    count_ones = len(list(buckets[1]))
    count_threes = len(list(buckets[3]))

    return count_ones * count_threes


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
    print(f"{part_one(data)}")
    print(f"{part_two()}")
