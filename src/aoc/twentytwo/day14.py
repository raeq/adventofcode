from collections import deque

from aoc.utils.matrix import Matrix, Point


def get_data(fn):
    paths: list = []
    max_y: int = 0
    min_x: int = 1000000
    max_x: int = 0

    with open(fn, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            items: deque = deque()
            for i in [x for x in line.split(' -> ')]:
                parts = list(map(int, i.split(',')))
                if parts[0] < min_x:
                    min_x = parts[0]
                if parts[0] > max_x:
                    max_x = parts[0]
                if parts[1] > max_y:
                    max_y = parts[1]
                i = Point(parts[0], parts[1], 0)
                items.append(i)
            paths.append(items)

    p: Point
    for q in paths:
        for p in q:
            p.x = p.x - (max_x - min_x)
            print(p)

    return paths, (max_y, min_x, max_x)


def populate_rocks(m: Matrix, path_data: list):
    data2: deque
    for data2 in path_data:
        while data2:
            print(data2.pop())
        print()


if __name__ == '__main__':
    fn = "day14.txt"
    data, maxima = get_data(fn)
    print(maxima)
    rebase = maxima[2] - maxima[1]

    empty_data: list[list[int]] = [[0] * 173] * (rebase)

    m: Matrix = Matrix(matrix=empty_data)

    populate_rocks(m, data)
