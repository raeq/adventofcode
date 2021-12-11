from functools import reduce


CLOSING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

CORRUPTED_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def syntax_scores(error):
    for line in DATA:
        close_queue = []

        for token in line:
            if token in CLOSING:
                close_queue.append(CLOSING[token])
            elif close_queue[-1] == token:
                close_queue.pop()
            else:
                if error == "corrupted":
                    yield CORRUPTED_POINTS[token]
                break
        else:
            if error == "incomplete":
                yield reduce(
                    lambda total, points: 5 * total + points,
                    map(INCOMPLETE_POINTS.get, reversed(close_queue)),
                    0,
                )


def part_one():
    return sum(syntax_scores(error="corrupted"))


def part_two():
    scores = sorted(syntax_scores(error="incomplete"))
    return scores[len(scores) >> 1]


if __name__ == '__main__':
    DATA = [x.strip() for x in open("day10.txt").readlines()]
    print(part_one())
    print(part_two())
