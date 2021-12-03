import logging
from typing import NamedTuple

from aoc.utils.decorator_utils import invocation_log


log = logging.getLogger("aoc")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


class Position(NamedTuple):
    x: int
    y: int
    z: int

    def __repr__(self):
        return f'Position(x = {self.x}, y = {self.y}, z = {self.z})'


class Submarine:
    position: Position
    _aim: int

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self._aim = 0
        self.position = Position(x=x, y=y, z=z)

    def __repr__(self):
        return f'Submarine(x = {self.position.x}, y = {self.position.y}, z = {self.position.z})'

    @invocation_log
    @property
    def depth(self) -> int:
        return self.position.z

    @invocation_log
    def forward(self, distance: int):
        ...

    @invocation_log
    def up(self, distance: int):
        ...

    @invocation_log
    def down(self, distance: int):
        ...

    @invocation_log
    def move(self, direction: str, distance: int):
        ...


sub = Submarine()
print(sub)
