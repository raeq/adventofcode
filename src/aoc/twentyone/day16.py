from functools import reduce
from operator import *


with open('day16.txt', 'r') as f:
    data = f.read().strip()

bits = [(int(c, 16) >> (3 - i)) & 1 for c in data for i in range(4)][::-1]


def as_num(bits):
    return reduce(lambda x, y: (x << 1) | y, bits)


def read_bits(data, n):
    for _ in range(n):
        yield data.pop()


def read_num(data, n):
    return as_num(read_bits(data, n))


vnum_total = 0


def decode(data):
    global vnum_total
    version = read_num(data, 3)
    vnum_total += version
    type_id = read_num(data, 3)

    def get_subpackets():
        if type_id == 4:
            while True:
                done = not data.pop()
                yield read_num(data, 4)
                if done:
                    return
        lid = data.pop()
        if lid:
            for _ in range(read_num(data, 11)):
                yield decode(data)
        else:
            blen = read_num(data, 15)
            l1 = len(data) - blen
            while len(data) != l1:
                yield decode(data)

    f = [add, mul, min, max, lambda x, y: (x << 4) | y, gt, lt, eq][type_id]
    return reduce(f, get_subpackets())


print(decode(bits))
print(vnum_total)
