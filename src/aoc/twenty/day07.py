import typing
from collections import defaultdict
from functools import lru_cache

import regex as re

bags: dict = defaultdict(dict)


def load_file(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as fd:
        return [line.rstrip("\n") for line in fd]


def parse_data(line: str) -> dict:
    regex = r"^(\b\S*\b\s\b\S*\b) bags"
    matches = re.findall(regex, line, re.IGNORECASE | re.DOTALL)
    for m in matches:

        if "no other" not in line:
            regex = r"(\b\d\b)\s(\b\S*\b\s\b\S*\b)"
            matches = re.findall(regex, line, re.IGNORECASE | re.DOTALL)
            for b in matches:
                bags[m][b[1]] = int(b[0])
        else:
            pass
            # bags[m] = ""
    return bags


@lru_cache()
def find_all_outer(bag) -> set:
    outer_bags = set()

    for key_bag in bags:
        if bag in bags[key_bag]:
            outer_bags.add(key_bag)
            outer_bags.update(find_all_outer(key_bag))
    if outer_bags:
        return outer_bags

    return {bag}


@lru_cache()
def find_all_inner(bag) -> int:
    inner_bags = 0

    for value_bag in bags[bag]:
        quantity = bags[bag][value_bag]
        inner_bags += quantity
        inner_bags += quantity * find_all_inner(value_bag)

    return inner_bags


def main():
    for d in load_file("day07.txt"):
        parsed = parse_data(d)
        bags.update(parsed)

    print(f"Part one answer: {len(find_all_outer('shiny gold'))}")
    print(f"Part two answer: {find_all_inner('shiny gold')}")


if __name__ == "__main__":
    main()
