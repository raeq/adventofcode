def get_data(filename: str) -> list:
    return_list: list = []

    with open(filename, 'r') as f:
        for line in f:
            return_list.append(tuple(line.split()))

    return return_list


if __name__ == "__main__":
    data = get_data("day01.txt")
