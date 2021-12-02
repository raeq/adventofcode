from collections import defaultdict

def get_data(fn):
    data: list = []
    with open(fn) as f:
        for line in f:
            data.append(line.rstrip().split())
    return data


class Submarine:
    x: int
    y: int
    z: int
    _aim: int
    _history: list
    _sequences: dict

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self._aim = 0
        self._history = []
        self._sequences = defaultdict(list)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}(x = {self.x}, y = {self.y}, z = {self.z})'

    def forward(self, value: int):
        self.x += value
        self.z += self._aim * value

    def up(self, value: int):
        self._aim -= value

    def down(self, value: int):
        self._aim += value

    def move(self, function_name, distance):
        distance = int(distance)
        self._history.append((function_name, distance))
        self._sequences[function_name].append(distance)
        return getattr(self, function_name)(distance)


if __name__ == "__main__":
    data = get_data("day02.txt")

    sub = Submarine()
    for direction, value in data:
        sub.move(direction, value)
        print(sub)

    ans = sum(sub._sequences["forward"]) * (sum(sub._sequences["down"]) - sum(sub._sequences["up"]))
    print(f'Day 1 Part 1 answer: '
          f'{ans}'
          )
    print(f'Day 1 Part 2 answer: {sub.x * sub.z}')
