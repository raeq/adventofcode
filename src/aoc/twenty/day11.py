from itertools import count, product

import numpy as np
from scipy.ndimage import convolve

FLOOR, EMPTY, OCCUPIED = -1, 0, 1


def load_file(file_name: str) -> str:
    with open(file_name, "r") as fd:
        return fd.read()


def parse_raw(raw: str):
    trans = {".": FLOOR, "L": EMPTY}
    return np.array([[trans[char] for char in line] for line in raw.splitlines()])


def part_one():
    KERNEL = [[OCCUPIED, OCCUPIED, OCCUPIED],
              [OCCUPIED, EMPTY, OCCUPIED],
              [OCCUPIED, OCCUPIED, OCCUPIED]]
    last = None
    seats = data
    while (as_bytes := seats.tobytes()) != last:
        last = as_bytes
        neighbors = convolve(np.where(floor, 0, seats), KERNEL, mode="constant")
        seats = np.where(floor, FLOOR,
                         np.where(neighbors >= 4, EMPTY, np.where(neighbors == 0, OCCUPIED, seats)))
    return (seats == OCCUPIED).sum()


def check_line(y, x, y_step, x_step, seats):
    if y_step == x_step == 0:
        return 0

    for i in count(1):
        cell_y, cell_x = y + i * y_step, x + i * x_step
        if cell_y not in range(0, h) or cell_x not in range(0, w):
            return 0
        if (cell := seats[cell_y, cell_x]) != -1:
            return cell


def part_two():
    last = None
    seats = data
    while (as_bytes := seats.tobytes()) != last:
        last = as_bytes
        neighbors = np.zeros_like(data)
        it = np.nditer(data, flags=["multi_index"])
        for seat in it:
            y, x = it.multi_index
            if seat == FLOOR:
                neighbors[y, x] = FLOOR
            else:
                neighbors[y, x] = sum(
                    check_line(y, x, i, j, seats) for i, j in product((-1, 1, 0), repeat=2))
        seats = np.where(neighbors >= 5, EMPTY, np.where(neighbors == 0, OCCUPIED, seats))

    return (seats == OCCUPIED).sum()


if __name__ == "__main__":
    data = parse_raw(load_file("day11.txt"))

    floor = data == -1
    h, w = data.shape

    print(part_one())
    print(part_two())
