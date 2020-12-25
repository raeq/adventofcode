PRIME: int = int(20201227)
INITIALIZATION_VECTOR: int = int(7)


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return tuple(map(int, fd.read().split('\n')))


def get_secret_loop_size(cardkey: int, doorkey: int) -> tuple[int, int]:
    for n in range(1, PRIME):
        if pow(INITIALIZATION_VECTOR, n, PRIME) == cardkey:
            return n, pow(doorkey, n, PRIME)


def main():
    CARD_PUBLIC_KEY, DOOR_PUBLIC_KEY = load_file("day25.txt")
    iterations, handshake = get_secret_loop_size(cardkey=CARD_PUBLIC_KEY, doorkey=DOOR_PUBLIC_KEY)
    print(f"Loop size: {iterations}, handshake: {handshake}")


if __name__ == '__main__':
    main()
