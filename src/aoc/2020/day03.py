from collections import namedtuple as nt

import math


def load_file(file_name: str):
    lines: list = []
    with open(file_name) as fd:
        for line in fd:
            lines.append(line.strip())
    return lines


def traverse(right_steps=3, down_steps=1):
    trees: int = 0
    for i in range(0, height, down_steps):
        location: int = i // down_steps * right_steps % width
        trees += 1 if fields[i][location] == "#" else 0
    return trees


if __name__ == "__main__":

    Rule: nt = nt('Rule', ['right_steps', 'down_steps'])

    fields = load_file("day03.txt")
    height = len(fields)
    width = len(fields[0])
    print(f"Data Width: {height}")
    print(f"Data Height: {width}\n")

    trees_per_run = []
    rules = [Rule(right_steps=1, down_steps=1),
             Rule(right_steps=3, down_steps=1),
             Rule(right_steps=5, down_steps=1),
             Rule(right_steps=7, down_steps=1),
             Rule(right_steps=1, down_steps=2)]

    # Part 1
    rule = rules[1]
    trees: int = traverse(rule.right_steps, rule.down_steps)
    print("Part 1")
    print(f"Run '{rule}' number of trees: {trees}\n")

    # Part 2
    print("Part 2")
    for rule in rules:
        trees: int = traverse(rule.right_steps, rule.down_steps)
        trees_per_run.append(trees)
        print(f"Run '{rule}' number of trees: {trees}")

    print(f"\nProduct: {math.prod(trees_per_run)}")
