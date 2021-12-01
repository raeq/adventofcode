with open("day01.txt") as f:
    depths = [int(x.strip()) for x in f]

part1 = sum(y > x for x, y in zip(depths, depths[1:]))
part2 = sum(y > x for x, y in zip(depths, depths[3:]))

print(part1, part2, sep="\n")
