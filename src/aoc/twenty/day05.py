"""
For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column.
In this example, the seat has ID 44
* 8 + 5 = 357.

As a sanity check, look through your list of boarding passes.
What is the highest seat ID on a boarding pass?
"""

import logging


log = logging.getLogger('custom_log')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


def load_file(file_name: str) -> str:
    with open(file_name, 'r') as fd:
        return [line.rstrip('\n') for line in fd]


def calc_seat(boarding_pass: str) -> int:
    log.debug(f"calc seat {boarding_pass}")
    seat_raw = boarding_pass[-3:]
    seat_bin = seat_raw.replace('L', '0').replace('R', '1')
    seat_dec: int = int(seat_bin, 2)

    log.info(f"Seat: original: {seat_raw} binary {seat_bin} decimal {seat_dec}")
    return seat_dec


def calc_row(boarding_pass: str) -> int:
    log.debug(f"calc row {boarding_pass}")
    row_raw = boarding_pass[:7]
    row_bin = row_raw.replace('F', '0').replace('B', '1')
    row_dec: int = int(row_bin, 2)

    log.info(f"Row original: {row_raw} binary {row_bin} decimal {row_dec}")
    return row_dec


def seat_id(boarding_pass: str) -> int:
    log.debug(f"seat id {boarding_pass}")
    row = calc_row(boarding_pass)
    seat = calc_seat(boarding_pass)

    seatid = row * 8 + seat

    log.info(f"Seat id, row: {row} seat: {seat} id: {seatid}")
    return seatid


def get_seats() -> list:
    filename = "day05.txt"
    fields = load_file(filename)
    seats: list = []

    for bp in fields:
        seats.append(seat_id(bp))
    log.info(f"There are {len(seats)} lines in the file {filename}")
    return seats


def find_empty(seats: list) -> int:
    cur = 0
    previous = 0
    next = 0

    candidate1: int = None
    candidate2: int = None

    for i in range(1, len(seats) - 1, 1):
        seat_val: int = seats[i]
        seat_val_prev: int = seats[i - 1]
        seat_val_next: int = seats[i + 1]

        if seat_val != seat_val_prev + 1:
            candidate1 = seat_val - 1
            log.info(f"A This seat {seat_val} is not +1 the previous seat {seat_val_prev} candidate1: {candidate1}")

        if seat_val != seat_val_next - 1:
            candidate2 = seat_val + 1
            log.info(f"B This seat {seat_val} is not 1- the next seat {seat_val_next} candidat2: {candidate2}")

            return candidate2


if __name__ == "__main__":
    log.debug(__name__)
    seats = get_seats()

    print(f"Highest found: {max(seats)}")
    print(f"My seat number: {find_empty(sorted(seats))}")

    print("Answer:", seat_id("FBFBBFFRLR"))
    print("Answer:", seat_id("BFFFBBFRRR"))
    print("Answer:", seat_id("FFFBBBFRRR"))
    print("Answer:", seat_id("BBFFBBFRLL"))
