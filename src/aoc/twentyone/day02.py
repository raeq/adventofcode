from collections import defaultdict


def get_data(fn):
    with open(fn) as f:
        data = [x.rstrip().split() for x in f]
        for value in data:
            value[1] = int(value[1])

    return data


class Submarine:
    x: int
    y: int
    z: int
    _aim: int

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self._aim = 0
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}(x = {self.x}, y = {self.y}, z = {self.z})'

    def forward(self, distance: int):
        self.x += distance
        self.z += self._aim * distance

    def up(self, distance: int):
        self._aim -= distance

    def down(self, distance: int):
        self._aim += distance

    def move(self, function_name, distance):
        return getattr(self, function_name)(distance)


if __name__ == "__main__":
    data = get_data("day02.txt")

    moves: dict = defaultdict(list)
    for direction, distance in data:
        moves[direction].append(distance)

    loc: int = sum(moves["forward"]) * (sum(moves["down"]) - sum(moves["up"]))
    print(f'Day 1 Star 1 answer: {loc}')

    sub = Submarine()
    for direction, distance in data:
        sub.move(direction, distance)

    print(f'Day 1 Part 2 answer: {sub.x * sub.z}')
