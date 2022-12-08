from itertools import chain

from more_itertools import chunked


def transpose_rows_to_columns(rows) -> list:
    return [list(i) for i in zip(*rows)]


def get_data(fn):
    numbers, *boards = open(fn).read().split('\n\n')
    numbers = [int(x) for x in numbers.split(',')]
    boards = [[[*map(int, r.split())] for r in b.split('\n')] for b in boards]
    return numbers, boards


def is_number_in_board(number, board):
    return number in board["set"]


def remove_number_from_board(number, board):
    if is_number_in_board(number, board):
        l: list = board["flat_board"]
        l[l.index(number)] = True
        l: list = board["rotated_board"]
        l[l.index(number)] = True


def is_winner(board: dict):
    for ch in chunked(board["flat_board"], 5):
        if all([True if x is True else False for x in ch]): return True, "flat_board"
    for ch in chunked(board["rotated_board"], 5):
        if all([True if x is True else False for x in ch]): return True, "rotated_board"
    return False, ""


def solve1():
    drawn: list = []
    for key, board in boards_dict.items():
        for num in numbers:
            drawn.append(num)
            remove_number_from_board(num, board)
            wins, key = is_winner(board)
            if wins:
                mysum = sum([x for x in board[key] if x is not True])
                break
    return mysum * num, board


def main():
    for idx, board in enumerate(boards):
        boards_dict[idx] = {}
        boards_dict[idx]["set"] = set(chain(*board))
        boards_dict[idx]["board"] = board
        boards_dict[idx]["flat_board"] = list(chain(*board))
        boards_dict[idx]["rotated_board"] = list(chain(*transpose_rows_to_columns(board)))


if __name__ == "__main__":
    numbers, boards = get_data("day04.txt.txt")
    boards_dict: dict = {}

    main()
    print(f'Day 4 part 1 ans: {solve1()}')  # 49686
    # print(solve2())  # 26878
