import collections
import operator
from collections import deque
from math import lcm, prod

import regex as re


class PackItem:
    __slots__ = "worry_level"

    worry_level: int

    def __init__(self, worry_level: int):
        self.worry_level = int(worry_level)


class Monkey:
    parser = None
    items: deque[PackItem] = None
    id: int = None
    count: int

    class Parse:
        id: int = None
        items: deque = None
        right_operand: int = None
        operation = None
        modulo_test: int = None
        true_target: int = None
        false_target: int = None

        def __init__(self, raw_monkey_data2: str):
            lines = []
            self.items = deque()

            for line in raw_monkey_data2.rstrip().split("\n"):
                lines.append(line.strip())

            line = lines[0]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.id = int(matches[0])

            line = lines[1]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            for worry_level in matches:
                self.items.append(PackItem(worry_level))

            line: str = lines[2]
            if "old * old" in line:
                self.right_operand = 2
                self.operation = operator.ipow
            else:
                self.right_operand = int(line.split()[-1])
                if " + " in line:
                    self.operation = operator.add
                elif " * " in line:
                    self.operation = operator.mul

            line = lines[3]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.modulo_test = int(matches[0])

            line = lines[4]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.true_target = int(matches[0])

            line = lines[5]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.false_target = int(matches[0])

    def __init__(self, raw_monkey_data1: str):
        self.parser: Monkey.Parse = Monkey.Parse(raw_monkey_data1)
        self.id = self.parser.id
        self.items = self.parser.items
        self.count = 0

    def inspect(self, an_lcm: int = None):

        for _ in range(len(self.items)):
            i = self.items.popleft()
            self.count += 1

            i.worry_level = self.parser.operation(i.worry_level, self.parser.right_operand)
            if an_lcm:
                i.worry_level = i.worry_level % an_lcm
            else:
                i.worry_level = i.worry_level // 3

            target: int = None
            if i.worry_level % self.parser.modulo_test:
                target = self.parser.false_target
            else:
                target = self.parser.true_target

            yield target, i



class MonkeyHouse(collections.UserList):
    def __init__(self, _iterable=None):
        if _iterable:
            super().__init__(
                item for item in _iterable if isinstance(item, Monkey))
        else:
            super().__init__()
        self._lcm: int = None

    def insert(self, index, item):
        if isinstance(item, Monkey):
            super().insert(index, item)
        else:
            raise TypeError('Item must be a Monkey.')

    def __setitem__(self, index, item):
        if isinstance(item, Monkey):
            super().__setitem__(index, item)
        else:
            raise TypeError('Item must be a Monkey.')

    def append(self, item):
        if isinstance(item, Monkey):
            super().append(item)
        else:
            raise TypeError('Item must be a Monkey.')

    def extend(self, other):
        if isinstance(other, Monkey):
            super().extend(other)
        elif isinstance(other, MonkeyHouse):
            super().extend(item for item in other)

    def rounds(self, iterations: int = 0):
        m: Monkey
        for _ in range(iterations):
            for m in self.data:
                for target, item in m.inspect():
                    self.data[target].items.append(item)

    @property
    def lowest_common_multiple(self) -> int:
        if not self._lcm:
            self._lcm = lcm(*[x.parser.modulo_test for x in self.data])
        return self._lcm

    def rounds_fast(self, iterations: int = 0):
        m: Monkey
        for _ in range(iterations):
            for m in self.data:
                for target, item in m.inspect(an_lcm=self.lowest_common_multiple):
                    self.data[target].items.append(item)

    @property
    def top_two_mul(self) -> int:
        s = [m.count for m in sorted(self.data, key=lambda x: x.count, reverse=True)[:2]]
        return prod(s)


def get_data(fn: str):
    mh = MonkeyHouse()

    with open(fn, 'r') as f:
        raw_data = f.read().rstrip().split("\n\n")

    for idx, m in enumerate(raw_data):
        mh.append(Monkey(m))

    return mh


def main(fn: str):
    monkey_house: MonkeyHouse = get_data(fn)
    monkey_house.rounds(20)
    print(f"Day 11 part 1: {monkey_house.top_two_mul}")

    monkey_house: MonkeyHouse = get_data(fn)
    monkey_house.rounds_fast(10_000)
    print(f"Day 11 part 2: {monkey_house.top_two_mul}")


if __name__ == "__main__":
    main("day11.txt")
