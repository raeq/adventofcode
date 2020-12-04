import logging
from collections import namedtuple as nt
from functools import lru_cache

from aoc.utils.decorator_utils import timing
from aoc.utils.log import logwith


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return [line.rstrip('\n') for line in fd]


@lru_cache()
@logwith()
def traverse(right_steps: int, down_steps: int) -> int:
    trees_found: int = 0
    for i in range(0, height, down_steps):
        location: int = i // down_steps * right_steps % width
        trees_found += 1 if fields[i][location] == "#" else 0
    return trees_found


@timing
def main():
    global fields
    global height
    global width

    Rule: nt = nt('Rule', ['right_steps', 'down_steps'])

    fields = load_file("day03.txt")
    height = len(fields)
    width = len(fields[0])
    print(f"Data Width: {height}")
    print(f"Data Height: {width}\n")

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
    trees_product: int = 1
    for rule in rules:
        trees: int = traverse(rule.right_steps, rule.down_steps)
        trees_product = trees_product * trees
        print(f"Run '{rule}' number of trees: {trees}")

    print(f"\nProduct: {trees_product}")


if __name__ == "__main__":
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    main()
