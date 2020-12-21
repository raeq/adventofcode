def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:

        data = [_.strip().replace(")", "").split('(contains') for _ in fd.readlines()]
        for _ in data:
            _[0] = set(_[0].strip().split(" "))
            _[1] = set(_[1].strip().split(","))

        return data



def main():
    data = load_file("day21.txt")
    print(data)

if __name__ == '__main__':
    main()