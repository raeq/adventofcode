"""
# Git Ident: '$Id$'
"""

from dataclasses import dataclass, field

import regex as re


@dataclass
class Person:
    answers: set = field(default_factory=set)

    def __init__(self, raw_record: str):
        self.raw_record = raw_record
        self.answers = set(raw_record)


@dataclass
class Group:
    persons: list = field(default_factory=list)
    answer_count: int = 0
    unanimous_count: int = 0

    def __init__(self, raw_record: str):
        self.raw_data = raw_record.strip().split('\n')
        self.persons = []

        for record in self.raw_data:
            self.persons.append(Person(record))

        self.answer_count = self.group_distinct_answers()
        self.unanimous_count = self.group_unanimous_answers()

    def group_distinct_answers(self) -> int:
        ans = set()
        p: Person

        for p in self.persons:
            ans = ans.union(p.answers)

        return len(ans)

    def group_unanimous_answers(self) -> int:

        ans: list = []
        for p in self.persons:
            ans.append(p.answers)
        ans = ans[0].intersection(*ans)

        return len(ans)


def load_file(file_name: str) -> str:
    with open(file_name, "r") as fd:
        return fd.read()


def get_data(full_text: str):
    regex = r"(.*?)\n\n"
    matches = re.finditer(regex, full_text, re.IGNORECASE | re.DOTALL)

    my_groups: list = []

    for match in matches:
        for g in match.groups():
            my_groups.append(Group(raw_record=g))
    return my_groups


def main():
    d = load_file("day06.txt")

    total_ans: int = 0
    total_unani: int = 0

    g: Group
    for g in get_data(d):
        total_ans += g.answer_count
        total_unani += g.unanimous_count

    print(f"Part 1 answer, sum of distinct answers: {total_ans:>5}")
    print(f"Part 2 answer, sum of unanimous answers: {total_unani:>4}")


if __name__ == "__main__":

    main()
