rules_day1 = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

rules_day2 = {
    "X": {"A": "Z", "B": "X", "C": "Y"},  # lose
    "Y": {"A": "X", "B": "Y", "C": "Z"},  # draw
    "Z": {"A": "Y", "B": "Z", "C": "X"},  # win
}

my_shape = {"X": 1, "Y": 2, "Z": 3}
rounds_day1, rounds_day2 = [], []


def get_score_day1(p1, p2) -> int:
    result = rules_day1[p1][p2] + my_shape[p2]
    return result


def get_score_day2(p1, p2):
    my_play = rules_day2[p2][p1]
    result = get_score_day1(p1, my_play)
    return result


with open("day02.txt") as f:
    for line in f.readlines():
        p1, p2 = line.strip().split(" ")
        rounds_day1.append(get_score_day1(p1, p2))
        rounds_day2.append(get_score_day2(p1, p2))

print(f"Day 2 part 1 answer: {sum(rounds_day1)}")
print(f"Day 2 part 2 answer: {sum(rounds_day2)}")
