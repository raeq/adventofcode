from collections import defaultdict


def get_data(fn):
    data: list = []
    with open(fn) as f:
        for line in f:
            data.append(line.rstrip().split())
    return data


class Submarine:
    """
    A Submarine class. It can ``move()`` forward, up or down by a given value.
    It saves a history of movement commands received in _history.
    It also saves a dictionary of each command type, and the values received in _sequences.
    """
    x: int
    y: int
    z: int
    _aim: int
    _history: list
    _sequences: dict

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        """
        This initializer sets all the objects values to 0.
        """
        self._aim = 0
        self._history = []
        self._sequences = defaultdict(list)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """
        A method to be used by the repr() function.
        It's output can be used by eval() to recreate a comparable object.
        :return:
        :rtype: str
        """
        return f'{self.__class__.__name__}(x = {self.x}, y = {self.y}, z = {self.z})'

    def forward(self, value: int):
        """
        Move the submarine forwards along the given direction by the supplied value.
        """
        self.x += value
        self.z += self._aim * value

    def up(self, value: int):
        """
        Aim the submarine in a direction by the supplied value.
        """
        self._aim -= value

    def down(self, value: int):
        """
        Aim the submarine in a direction by the supplied value.
        """
        self._aim += value

    @property
    def forward_sum(self):
        return sum(self._sequences["forward"])

    @property
    def down_sum(self):
        return sum(self._sequences["down"])

    @property
    def up_sum(self):
        return sum(self._sequences["up"])

    def move(self, direction: str, distance: [int, str]):
        """
        Choose direction "up" or "down" or "forward" and supply a distance.
        """
        distance = int(distance)
        self._history.append((direction, distance))
        self._sequences[direction].append(distance)
        return getattr(self, direction)(distance)


if __name__ == "__main__":
    data = get_data("day02.txt")

    sub = Submarine()
    for direction, value in data:
        sub.move(direction, value)
        print(sub)

    print(f'Day 2 Part 1 answer: '
          f'{sub.forward_sum * (sub.down_sum - sub.up_sum)}')
    print(f'Day 2 Part 2 answer: {sub.x * sub.z}')
