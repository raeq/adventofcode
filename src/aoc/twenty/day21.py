from functools import reduce
from collections import defaultdict
import regex as re


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return fd.read()


def parse_raw(raw):
    ALLERGEN_RE = r"(.+) \(contains (.+)\)"
    foods = []
    contaminated = defaultdict(list)

    for ingredients, allergens in re.findall(ALLERGEN_RE, raw):
        ingredients = set(ingredients.split())
        foods.append(ingredients)
        for allergen in allergens.split(", "):
            contaminated[allergen].append(ingredients)
    return foods, {k: reduce(set.intersection, v) for k, v in contaminated.items()}




def part_one(foods, allergens):
    safe = reduce(set.union, foods) - reduce(set.union, allergens.values())
    return sum(ingredient in safe for food in foods for ingredient in food)


def part_two(allergens):
    stack = list(allergens.items())
    canonical = []
    while stack:
        stack.sort(key=lambda tup: -len(tup[1]))
        allergen, (ingredient,) = stack.pop()
        canonical.append((allergen, ingredient))
        for _, possible in stack:
            possible.discard(ingredient)
    return ",".join(ingredient for _, ingredient in sorted(canonical))


def main():
    print(f"Part one answer: {part_one(foods, allergens)}")
    print(f"Part two answer {part_two(allergens)}")

if __name__ == '__main__':
    raw = load_file("day21.txt")
    foods, allergens = parse_raw(raw)

    main()