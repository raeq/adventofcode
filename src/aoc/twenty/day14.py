from math import inf

import re
from sympy.ntheory.modular import crt


def load_file(file_name: str) -> []:
    with open(file_name, "r") as fd:
        return fd.read()


if __name__ == '__main__':
    my_data = load_file("day14.txt")
    print(f"Part one:{part_one(my_data)}")
    #print(f"Part two:{part_two(my_data[1])}")
