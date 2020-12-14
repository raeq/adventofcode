from math import inf

from sympy.ntheory.modular import crt


def load_file(file_name: str) -> []:
    with open(file_name, "r") as fd:
        return [_ for _ in fd.readlines()]


def part_one(early, avail):
    # Part 1
    early = int(early.strip())
    avail = [int(x) for x in avail.split(",") if x != "x"]
    ans = inf

    for y in avail:
        x = early
        while x % y != 0:
            x += 1
        if x < ans:
            yy = y
            ans = x

    return (ans - early) * yy


def part_two(avail):
    M, U = [], []
    for i, j in enumerate(avail.split(",")):
        if j == 'x':
            continue
        else:
            j = int(j)
            M.append(j)
            U.append(j - i)

    return crt(M, U)[0]


if __name__ == '__main__':
    my_data = load_file("day13.txt")
    print(f"Part one:{part_one(my_data[0], my_data[1])}")
    print(f"Part two:{part_two(my_data[1])}")
