import numpy as np
from scipy.ndimage import convolve


def evolve(inputs: np.array, kernel: np.array):
    for _ in range(GENERATIONS):
        neighbors = convolve(inputs, kernel, mode="constant")
        inputs = np.where((neighbors == 3) | (inputs & (neighbors == 2)), 1, 0)

    return inputs.sum()


def part_one(data):
    kernel: np.array = np.ones((3, 3, 3))
    kernel[1, 1, 1] = 0

    weights: np.array = np.zeros((13, 20, 20), dtype=int)
    weights[GENERATIONS] = np.pad(data, GENERATIONS)

    return evolve(weights, kernel)


def part_two(data):
    kernel: np.array = np.ones((3, 3, 3, 3))
    kernel[1, 1, 1, 1] = 0

    weights: np.array = np.zeros((13, 13, 20, 20), dtype=int)
    weights[GENERATIONS, GENERATIONS] = np.pad(data, GENERATIONS)

    return evolve(weights, kernel)


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return [_.strip() for _ in fd.readlines()]


def main():
    raw = load_file("day17.txt")
    data = np.array([[char == "#" for char in line] for line in raw], dtype=int)

    print(f" Part one solution: {part_one(data):>7}")
    print(f" Part two solution: {part_two(data):>7}")


if __name__ == '__main__':
    GENERATIONS = 6
    main()
