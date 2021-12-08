def parse(filename):
    with open(filename) as fh:
        data = []
        for line in fh:
            l, r = line.strip().split(' | ')
            data.append((l.split(), r.split()))
        return data


def get_output_values(data, output):
    D = {}
    data = [set(x) for x in sorted(data, key=len)]
    get = lambda cond: next(i for i in data if cond(i))

    D[1] = data[0]
    D[7] = data[1]
    D[4] = data[2]
    D[8] = data[-1]
    D[3] = get(lambda i: len(D[7] & i) == 3 and len(i) == 5)
    D[9] = get(lambda i: len(D[3] & i) == 5 and len(i) == 6)
    D[6] = get(lambda i: len(D[1] & i) == 1 and len(i) == 6)
    D[5] = get(lambda i: len(D[6] & i) == 5 and len(i) == 5)
    D[0] = get(lambda i: i != D[6] and i != D[9] and len(i) == 6)
    D[2] = get(lambda i: i != D[3] and i != D[5] and len(i) == 5)

    return [next(i for i, d in D.items() if set(item) == d) for item in output]


def part1(filename):
    data = parse(filename)

    counts = {i: 0 for i in range(10)}

    for train, test in data:
        vals = get_output_values(train, test)
        for v in vals:
            counts[v] += 1

    res = counts[1] + counts[4] + counts[7] + counts[8]
    print("Part 1:", res)


def part2(filename):
    data = parse(filename)

    counts = []

    for train, test in data:
        vals = get_output_values(train, test)
        counts.append(int("".join(map(str, vals))))

    res = sum(counts)
    print("Part 2:", res)


#####################################################################

part1('day08.txt')
part2('day08.txt')
