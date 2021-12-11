from itertools import count

import numpy as np
from scipy.ndimage import convolve


def int_grid(raw, np=True, separator=""):
    """
    Parse a grid of ints into a 2d list or numpy array (if np==True).
    """
    array = [
        [int(i) for i in (line.split(separator) if separator else line)]
        for line in raw.splitlines()
    ]

    if np:
        import numpy as np

        return np.array(array)


def step(octos):
    octos += 1

    flashed = np.zeros_like(octos, dtype=bool)
    while (flashing := ((octos > 9) & ~flashed)).any():
        octos += convolve(flashing.astype(int), KERNEL, mode="constant")
        flashed |= flashing

    octos[flashed] = 0
    return flashed.sum()


def part_one():
    octos = OCTOPI.copy()
    return sum(step(octos) for _ in range(100))


def part_two():
    octos = OCTOPI.copy()

    for i in count():
        if (octos == 0).all():
            return i

        step(octos)


if __name__ == '__main__':
    OCTOPI = int_grid(open("day11.txt").read())

    KERNEL = np.ones((3, 3), dtype=int)

    print(part_one())
    print(part_two())
