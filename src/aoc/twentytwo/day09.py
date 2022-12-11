def sgn(x):
    return (x > 0) - (x < 0)


DELTA = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
r = [(0, 0)] * 10
a = {(0, 0)}
b = {(0, 0)}

with open("day09.txt") as fin:
    for line in fin:
        d, s = line.rstrip().split()
        s = int(s)

        for _ in range(s):
            hx, hy = r[0]
            dx, dy = DELTA[d]
            r[0] = hx + dx, hy + dy

            for i in range(9):
                hx, hy = r[i]
                tx, ty = r[i + 1]
                dx, dy = hx - tx, hy - ty

                if dx ** 2 + dy ** 2 > 2:
                    r[i + 1] = tx + sgn(dx), ty + sgn(dy)

            a.add((r[1]))
            b.add((r[9]))

a1 = len(a)
a2 = len(b)
print(1, a1)
print(2, a2)
