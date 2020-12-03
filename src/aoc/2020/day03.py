from collections import namedtuple as nt


def load_file(file_name: str):
    with open(file_name, 'r') as fd:
        return [line.rstrip('\n') for line in fd]


def traverse(right_steps: int, down_steps: int):
    trees_found: int = 0
    for i in range(0, height, down_steps):
        location: int = i // down_steps * right_steps % width
        trees_found += 1 if fields[i][location] == "#" else 0
    return trees_found


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
    trees_product: int = 1
    for rule in rules:
        trees: int = traverse(rule.right_steps, rule.down_steps)
        trees_product = trees_product * trees
        print(f"Run '{rule}' number of trees: {trees}")

    print(f"\nProduct: {trees_product}")
