import math


def load_file(file_name: str):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def traverse(right=3, down_step=1):
    trees = 0
    for i in range(0, length, down_step):
        location: int = i // down_step * right % width
        trees += 1 if fields[i][location] == "#" else 0
    return trees


if __name__ == "__main__":
    fields = load_file("day03.txt")
    length = len(fields)
    width = len(fields[0])

    print(f"Field Width: {length}")
    print(f"Field Height: {width}\n")
    total_trees = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        total_trees.append(traverse(slope[0], slope[1]))

    [print(f"Run {x} number of trees: {y}") for x, y in enumerate(total_trees)]
    print(f"\nProduct: {math.prod(total_trees)}")
