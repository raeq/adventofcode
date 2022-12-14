from functools import total_ordering


@total_ordering
class Packet:

    def __init__(self, data: str):
        self._raw = data
        self.half: list = eval(data.strip())

    def __str__(self):
        return f'{self.half}'

    def __repr__(self):
        return f'{self.__class__.__name__}(data={self.half}'

    def compare(self, l, r) -> int:

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return -1
            elif l == r:
                return 0
            else:
                return 1

        elif isinstance(l, list) and isinstance(r, list):
            i = 0
            while i < len(l) and i < len(r):
                c = self.compare(l[i], r[i])
                if c == -1:
                    return -1
                if c == 1:
                    return 1
                i += 1
            if i == len(l) and i < len(r):
                return -1
            elif i == len(r) and i < len(l):
                return 1
            else:
                return 0

        elif isinstance(l, int) and isinstance(r, list):
            return self.compare([l], r)
        elif isinstance(l, list) and isinstance(r, int):
            return self.compare(l, [r])

        raise ValueError

    def __lt__(self, other):
        if self.compare(self.half, other.half) == -1:
            return True
        return False

    def __gt__(self, other):
        if self.compare(self.half, other.half) == 1:
            return True
        return False

    def __eq__(self, other):
        if self.compare(self.half, other.half) == 0:
            return True
        return False


class PairIterator:
    def __init__(self, pair):
        self._packets: list[Packet] = [pair.left, pair.right]
        self._index = 0

    def __next__(self) -> 'Packet':
        if self._index < len(self._packets):
            self._index += 1
            return self._packets[self._index - 1]

        raise StopIteration


class Pair:

    def __init__(self, left: Packet, right: Packet):
        self.left: Packet = left
        self.right: Packet = right

    @property
    def in_order(self) -> bool:
        return self.left < self.right

    def __iter__(self) -> PairIterator:
        return PairIterator(self)

    def __str__(self):
        return f'In order? {self.in_order}\n{str(self.left)}\n{str(self.right)}'


pairs: list[Pair] = []
packets: list[Packet] = []

if __name__ == '__main__':
    with open("day13.txt", 'r') as f:
        for pair in f.read().rstrip().split('\n\n'):
            l, r = [x for x in pair.split('\n')]
            pairs.append(Pair(Packet(l), Packet(r)))

    sum: int = 0
    for idx, pair in enumerate(pairs, 1):
        if pair.in_order:
            sum += idx
    print(f'Day 13 part 1 ans: {sum}')

    first: Packet = Packet('[[2]]')
    second: Packet = Packet('[[6]]')
    packets.append(first)
    packets.append(second)
    for pair in pairs:
        for packet in pair:
            packets.append(packet)

    packets.sort()
    p1 = packets.index(first) + 1
    p2 = packets.index(second) + 1
    print(f'Day 13 part 2 ans = {p1 * p2}')
