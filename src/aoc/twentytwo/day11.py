import operator
from collections import deque

import regex as re


class PackItem:
    worry_level: int

    def __init__(self, worry_level: int):
        self.holders = []
        self.worry_level = int(worry_level)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.worry_level=}, {self.holders=})"


class Monkey:
    parser = None
    items: deque[PackItem] = None
    id: int = None
    count: int

    class Parse:
        lines: list = None
        id: int = None
        items: deque = None
        right_operand: int = None
        operation = None
        modulo_test: int = None
        true_target: int = None
        false_target: int = None

        def __init__(self, raw_monkey_data2: str):
            self.lines = []
            self.items = deque()

            for line in raw_monkey_data2.rstrip().split("\n"):
                self.lines.append(line.strip())

            line = self.lines[0]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.id = int(matches[0])

            line = self.lines[1]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            for m in matches:
                self.items.append(PackItem(m))

            line: str = self.lines[2]
            if "old * old" in line:
                self.right_operand = 2
                self.operation = operator.ipow
            elif " + " in line:
                self.right_operand = int(line.split()[-1])
                self.operation = operator.add
            elif " * " in line:
                self.right_operand = int(line.split()[-1])
                self.operation = operator.mul

            line = self.lines[3]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.modulo_test = int(matches[0])

            line = self.lines[4]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.true_target = int(matches[0])

            line = self.lines[5]
            matches = re.findall(r"[\d]+", line, re.IGNORECASE | re.DOTALL)
            if len(matches):
                self.false_target = int(matches[0])

        def __str__(self):
            return f"{self.__class__.__name__}({self.id=}, {self.modulo_test=}, {self.true_target=}," \
                   f" {self.right_operand=}, {self.operation=}, {self.false_target=}, {self.items=})"

        def __repr__(self):
            return str(self)

    def __init__(self, raw_monkey_data1: str):
        self.parser: Monkey.Parse = Monkey.Parse(raw_monkey_data1)
        self.id = self.parser.id
        self.items = self.parser.items
        self.count = 0

    def do_round(self, divthree: bool = True):
        try:
            while i := self.items.popleft():
                self.count += 1

                if divthree:
                    i.worry_level = self.parser.operation(i.worry_level, self.parser.right_operand)
                    i.worry_level = i.worry_level // 3

                else:
                    # if we multiply naively we get: 79*17=1343 . Then 1343 modulo 13 is equal 4 .
                    # Note that if we take 79 modulo 13 (that is 1) and multiply it by 17 , we get 17 .
                    # Then taking 17 modulo 13 gives us the same value as before — that is 4 !
                    # We get the same result while dealing with smaller numbers, which is crucial for this task.

                    if self.parser.operation in (operator.add, operator.ipow):
                        i.worry_level = self.parser.operation(i.worry_level, self.parser.right_operand)

                    else:
                        a = i.worry_level % self.parser.modulo_test
                        i.worry_level = self.parser.operation(a, self.parser.right_operand)

                if i.worry_level % self.parser.modulo_test == 0:
                    monkeys[self.parser.true_target].items.append(i)
                else:
                    monkeys[self.parser.false_target].items.append(i)
        except IndexError:
            ...

    def __str__(self):
        return f"{self.__class__.__name__}({self.id}, {self.count=}, {self.parser})"

    def __repr__(self):
        return str(self)


monkeys: list = []


def get_data():
    monkeys: list = []

    with open("day11_test.txt", 'r') as f:
        raw_data = f.read().rstrip().split("\n\n")

    for idx, m in enumerate(raw_data):
        monkeys.append(Monkey(m))

    return monkeys


monkeys = get_data()
m: Monkey
for _ in range(20):
    for m in monkeys:
        m.do_round()

s = sorted(monkeys, key=lambda x: x.count, reverse=True)[:2]
print(s[0].count * s[1].count)

monkeys = get_data()
for _ in range(10000):
    for m in monkeys:
        m.do_round(divthree=False)

s = sorted(monkeys, key=lambda x: x.count, reverse=True)[:2]
print(s[0].count * s[1].count)
