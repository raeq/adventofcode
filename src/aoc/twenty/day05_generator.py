"""
Generate test data sets for the day 5 challenge.
"""
import logging
import random


log = logging.getLogger("aoc")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


def generate_data(startat: int) -> list:
    lowest = random.choice(range(startat, 30))
    highest = random.choice(range(650, 850))
    ints: list = [i for i in range(lowest, highest)]
    popped = ints.pop(random.choice(range(50, 750)))
    passes: list = []

    for i in ints:
        raw_bin: str = '{0:b}'.format(i).zfill(10)
        row_ = raw_bin[:7].replace('0', 'F').replace('1', 'B')
        seat_ = raw_bin[-3:].replace('0', 'L').replace('1', 'R')
        passes.append(row_ + seat_)

    # remove one from somewhere

    random.shuffle(passes)

    return passes, popped, highest


if __name__ == "__main__":
    passports, missing, highest = generate_data(10)
    print(f"Missing: {missing}\nHighest: {highest}\n{passports}")
