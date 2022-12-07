calories = []
raw = open("day01.txt").read()

for elf in raw.split("\n\n"):
    calories.append(sum([int(i.strip()) for i in elf.split("\n")]))

print(f"Day 1 part 1 answer: {max(calories)}")
print(f"Day 1 part 2 answer: {sum(sorted(calories, reverse=True)[:3])}")
