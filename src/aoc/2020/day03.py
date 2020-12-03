import math

def get_data01(filename: str) -> list:
    return_list: list = []
    counter: int = 0
    rule: tuple = (3, 1)

    with open(filename, 'r') as f:
        for line in f:
            if counter > 0:
                traverse_part1(line.strip(), counter, rule)
            return_list.append(line.strip())
            counter += 1
    return return_list


def get_data02(filename: str) -> list:

    with open(filename, 'r') as f:
        for line in f:
            return [l.strip() * 32 for l in f]

is_x: list = []


def traverse_part1(data: str, linenum: int, rule: tuple):

    current_location = math.prod([linenum, rule[0]])
    current_line = data

    #if current_location > (31 * linenum):
    current_line: str = data * 33

    ans: bool = True if current_line[current_location] == "#" else False
    is_x.append(ans)

    return current_location

def traverse_part2(data: str, linenum: int, rule: tuple):
    current_location = math.prod([linenum, rule[0]])
    current_line = data

    ans: bool = True if current_line[current_location] == "#" else False
    return ans

def traverse_lines(data:list):

    rules: list[tuple] = []
    rules.append([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

    line_counter = 0
    tuple_counter = 0


    for line in data:
        if tuple_counter > len(rules): tuple_counter = 0

        print(traverse_part2(line, line_counter, rules[tuple_counter][0]))


        line_counter += 1
        tuple_counter +=1

    pass


if __name__ == "__main__":
    results = (len(get_data01("day03.txt")))

    counter = 0
    for x in is_x:
        if x:
            counter +=1

    assert (counter == 198)
    print(counter)

