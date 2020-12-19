from lark import Lark, LarkError


def valid_messages(rules, messages, prepend: str = "1"):
    grammar = rules.translate(str.maketrans("0123456789", "abcdefghij"))
    parser = Lark(grammar, start="a")
    valid = len(messages)

    for message in messages:
        try:
            parser.parse(message)
        except LarkError:
            valid -= 1
    return valid


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return fd.read()


def main():
    data = load_file("day19.txt").split("\n\n")

    rules = data[0]
    messages = data[1]
    messages = messages.splitlines()

    print(f"Part one solution: {valid_messages(rules, messages):>5}")

    rules = rules.replace('8: 42', '8: 42 | 42 8').replace('11: 42 31', '11: 42 31 | 42 11 31')
    print(f"Part two solution: {valid_messages(rules, messages, '2'):>5}")


if __name__ == '__main__':
    main()
