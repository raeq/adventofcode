from collections import deque
from itertools import islice

import numpy as np


def load_file(file_name: str) -> tuple[deque[int], deque[int]]:
    with open(file_name, 'r') as fd:
        p1, p2 = fd.read().split("\n\n")

        p1 = deque(list(map(int, p1.strip().split('\n')[1:])))
        p2 = deque(list(map(int, p2.strip().split('\n')[1:])))

        return p1, p2


def game(input_a, input_b, recurse=True):
    seen = set()
    while input_a and input_b:
        if (s := (tuple(input_a), tuple(input_b))) in seen:
            return True
        seen.add(s)

        a, b = input_a.popleft(), input_b.popleft()
        if recurse and a <= len(input_a) and b <= len(input_b):
            sub_alice, sub_bob = deque(islice(input_a, a)), deque(islice(input_b, b))
            input_a.extend((a, b)) if game(sub_alice, sub_bob) else input_b.extend((b, a))
        else:
            input_a.extend((a, b)) if a > b else input_b.extend((b, a))

    return bool(input_a)


def part_one(a, b):
    game(a, b, recurse=False)
    return enum @ (a or b)


def part_two(a, b):
    game(a, b)
    return enum @ (a or b)


if __name__ == '__main__':
    alice, bob = load_file("day22.txt")
    enum = np.arange(len(alice) + len(bob), 0, -1)

    print(f"The answer to part one is {part_one(alice, bob):>12}")
    alice, bob = load_file("day22.txt")
    print(f"The answer to part two is {part_two(alice, bob):>12}")
