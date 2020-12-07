import typing
from collections import defaultdict
from pprint import pprint

import regex as re


def load_file(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as fd:
        return [line.rstrip("\n") for line in fd]


def parse_data(line: str) -> dict:
    bags: dict = defaultdict(dict)

    regex = r"^(\b\S*\b\s\b\S*\b) bags"
    matches = re.findall(regex, line, re.IGNORECASE | re.DOTALL)
    for m in matches:

        if "no other" not in line:
            regex = r"(\b\d\b)\s(\b\S*\b\s\b\S*\b)"
            matches = re.findall(regex, line, re.IGNORECASE | re.DOTALL)
            for b in matches:
                bags[m][b[1]] = b[0]
        else:
            bags[m] = "empty"
    return bags


def main():
    mybags: dict = defaultdict(dict)

    for d in load_file("day07.txt"):
        parsed = parse_data(d)
        mybags.update(parsed)

    pprint(mybags)


if __name__ == "__main__":
    main()
