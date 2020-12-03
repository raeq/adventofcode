from aoc.utils.decorator_utils import timing


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return [line.rstrip('\n') for line in fd]


@timing
def main():
    global fields
    global height
    global width

    fields = load_file("day03.txt")
    height = len(fields)
    width = len(fields[0])
    print(f"Data Width: {height}")
    print(f"Data Height: {width}\n")


if __name__ == "__main__":
    main()
