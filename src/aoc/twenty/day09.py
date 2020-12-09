import itertools


def load_file(file_name: str) -> []:
    with open(file_name, "r") as fd:
        return [int(l.strip()) for l in fd.readlines()]


def addends_in_previous_25(previous_25: list, target: int) -> bool:
    """
    >>> addends_in_previous_25([15, 2, 4, 8, 9, 5, 10, 23], 38)
    True
    >>> addends_in_previous_25([15, 2, 4, 8, 9, 5, 10, 23], 23)
    True
    >>> addends_in_previous_25([15, 2, 4, 8, 9, 5, 10, 23], 150)
    False
    >>> addends_in_previous_25([15, 2, 4, 8, 9, 5, 10, 23], 2)
    False
    """
    sums = {sum(c) for c in list(itertools.combinations(
        [x for x in (_ for _ in previous_25[-25:] if _ < target)], 2))}

    return target in sums


def part_one(data: list) -> tuple:
    for i in range(25, len(data)):
        if addends_in_previous_25(data[i - 25:i], data[i]):
            continue
        return data[i - 25:i], data[i]


def part_two(full_list: list, target: int) -> list:
    """
    [1, 5, 9, 12] == 27
    1 + 9 == 10
    >>> part_two([1, 5, 9, 12, 13, 60], 27)
    10
    """

    pruned_list = [_ for _ in full_list if _ < target]

    prefix_sum = [0]
    for n in pruned_list:
        prefix_sum.append(prefix_sum[-1] + n)

    for i in range(len(pruned_list)):
        for j in range(i + 2, len(pruned_list)):
            subSum = prefix_sum[j + 1] - prefix_sum[i]
            if subSum == target:
                subset = pruned_list[i:j]
                return min(subset) + max(subset)


def main():
    """
    >>> len(load_file("day09.txt"))
    1000
    """
    all_data = load_file("day09.txt")
    seq, ans = part_one(all_data)
    ans2 = part_two(all_data, ans)
    print(f"The answer to part 1 is {ans:>9}")
    print(f"The answer to part 2 is {ans2:>9}")


if __name__ == '__main__':
    main()
