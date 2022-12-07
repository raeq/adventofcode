import string

from more_itertools import chunked

rucksacks = []

with open("day03.txt") as f:
    for line in f.readlines():
        line = line.strip()
        halfway = len(line) // 2
        rucksacks.append([set(line), list(set(line[:halfway]).intersection(set(line[halfway:])))])


def get_priority(common_item) -> int:
    if common_item in string.ascii_lowercase:
        return string.ascii_lowercase.index(common_item) + 1
    else:
        return string.ascii_uppercase.index(common_item) + 27


priorities_day1 = map(get_priority, [val[1][0] for val in rucksacks])

priorities_day2 = 0
for a, b, c in chunked(rucksacks, 3):
    priorities_day2 += get_priority(list(a[0].intersection(b[0].intersection(c[0])))[0])

print(f"Day 3 part 1 answer: {sum(list(priorities_day1))}")
print(f"Day 3 part 2 answer: {priorities_day2}")
