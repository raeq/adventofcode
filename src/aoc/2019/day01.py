def fuel(weight):
    return max(0, (int(weight) // 3) - 2)


def compound_fuel(mass):
    mass = int(mass)
    total_mass = 0

    while (mass := fuel(mass)) > 0: total_mass += mass

    return total_mass


def get_data(filename: str) -> list:
    ans0: int = 0
    ans1: int = 0

    with open(filename, 'r') as f:
        for line in f:
            ans0 += fuel(line)
            ans1 += compound_fuel(line)

    return ans0, ans1


if __name__ == "__main__":
    ans = get_data("day01.data.txt")
    print(ans[0], ans[1])
