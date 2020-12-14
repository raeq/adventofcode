import itertools
from collections import defaultdict


def load_file(file_name: str) -> []:
    with open(file_name, "r") as fd:
        return [_.strip() for _ in fd.readlines()]


def part_one(lines):
    m = defaultdict(int)
    for line in lines:
        a, b = line.split(" = ")
        if a == "mask":
            mask = b
        else:
            a = int(a[4:-1])
            b = int(b)
            v = 0
            for i in range(36):
                c = mask[-i - 1]
                if c == '1' or (c == 'X' and (b & (1 << i)) > 0):
                    v |= (1 << i)

            m[a] = v

    return sum(m.values())


def part_two(lines):
    m = defaultdict(int)
    for line in lines:
        a, b = line.split(" = ")
        if a == "mask":
            mask = b
        else:
            a = int(a[4:-1])
            b = int(b)
            v = 0
            extra = []
            for i in range(36):
                c = mask[-i - 1]
                if c == 'X':
                    extra.append(1 << i)
                elif c == '1' or (a & (1 << i)) > 0:
                    v += (1 << i)

            for k in range(len(extra) + 1):
                for c in itertools.combinations(extra, k):
                    s = sum(c)
                    m[v + s] = b

    return sum(m.values())


if __name__ == '__main__':
    my_data = load_file("day14.txt")
    print(f"Part one: {part_one(my_data):>20}")
    print(f"Part two: {part_two(my_data):>20}")
