counter_day1 = 0
counter_day2 = 0
with open("day04.txt") as f:
    for line in f.readlines():
        line = line.strip()
        a, b = line.split(",")
        a, b = list(map(int, a.split("-"))), list(map(int, b.split("-")))
        a = set(list(range(a[0], a[1] + 1)))
        b = set(list(range(b[0], b[1] + 1)))

        if a.issubset(b) or a.issuperset(b):
            counter_day1 += 1

        if a.intersection(b):
            counter_day2 += 1

print(f"Day 4 part 1: {counter_day1}")
print(f"Day 4 part 2: {counter_day2}")
