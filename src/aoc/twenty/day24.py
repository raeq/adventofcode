import re


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return fd.read()


def decode(tile):
    return sum(map(STEPS.__getitem__, tile))


def init_config(raw):
    DIRECTION_RE = re.compile(r"nw|ne|sw|se|w|e")
    tiles = (DIRECTION_RE.findall(line) for line in raw.splitlines())

    black = set()
    for tile in tiles:
        black ^= set((decode(tile),))
    return black


def neighbors(tile, with_self=False):
    if with_self: yield tile
    yield from (tile + neighbor for neighbor in STEPS.values())


def update(n, b):
    seen = set()
    flip = set()
    for _ in range(n):
        for tile in b:
            for neighbor in neighbors(tile, with_self=True):
                if neighbor in seen:
                    continue
                seen.add(neighbor)

                s = sum(map(b.__contains__, neighbors(neighbor)))
                if neighbor in b and (s == 0 or s > 2) or neighbor not in b and s == 2:
                    flip.add(neighbor)

        b.symmetric_difference_update(flip)
        seen.clear()
        flip.clear()


def part_one(b):
    return len(b)


def part_two(b):
    update(100, b)
    return len(b)


if __name__ == '__main__':
    STEPS = {
        "e": 0 + 2j,
        "w": 0 - 2j,
        "se": 1 + 1j,
        "sw": 1 - 1j,
        "ne": -1 + 1j,
        "nw": -1 - 1j,
    }

    raw = load_file("day24.txt")
    black = init_config(raw)
    print(f"The answer to part one is: {part_one(black):>6}")
    print(f"The answer to part two is: {part_two(black):>6}")
