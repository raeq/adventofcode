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
import typing

from aoc.utils.decorator_utils import invocation_log


log = logging.getLogger("aoc")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


def load_file(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as fd:
        return [line.rstrip("\n") for line in fd]


@invocation_log
def calc_seat(boarding_pass: str) -> int:
    """
    >>> calc_seat('FBFBBFFRLR')
    5
    """
    seat_raw = boarding_pass[-3:]
    seat_bin = seat_raw.replace("L", "0").replace("R", "1")
    seat_dec: int = int(seat_bin, 2)

    log.debug(f"Seat: original: {seat_raw} binary {seat_bin} decimal {seat_dec}")
    return seat_dec


@invocation_log
def calc_row(boarding_pass: str) -> int:
    """
    >>> calc_row('FBFBBFFRLR')
    44
    """
    row_raw = boarding_pass[:7]
    row_bin = row_raw.replace("F", "0").replace("B", "1")
    row_dec: int = int(row_bin, 2)

    log.debug(f"Row original: {row_raw} binary {row_bin} decimal {row_dec}")
    return row_dec


@invocation_log
def seat_id(boarding_pass: str) -> int:
    """
    >>> seat_id('FBFBBFFRLR')
    357
    >>> seat_id('BFFFBBFRRR')
    567
    >>> seat_id('FFFBBBFRRR')
    119
    >>> seat_id('BBFFBBFRLL')
    820
    """

    row = calc_row(boarding_pass)
    seat = calc_seat(boarding_pass)

    seatid = row * 8 + seat

    log.info(f"Seat id, raw: '{boarding_pass}' row: {row} seat: {seat} id: {seatid}")
    return seatid


@invocation_log
def get_seats() -> list:
    filename: str = "day05.txt"
    fields: list = load_file(filename)
    seat_numbers: list = []

    for bp in fields:
        seat_numbers.append(seat_id(bp))
    log.info(f"There are {len(seat_numbers)} lines in the file {filename}")
    return seat_numbers


@invocation_log
def find_empty(all_seats: list) -> int:
    """
    >>> find_empty([3,4,5,7,8])
    6
    """
    log.debug(f"Min value is {min(all_seats)}")
    log.debug(f"Max value is {max(all_seats)}")

    maximum_seats: set = {val for val in range(min(all_seats), max(all_seats))}
    diff: int = list(maximum_seats.difference(set(all_seats)))[0]

    log.info(f"The set difference is {diff}")
    return int(diff)


if __name__ == "__main__":
    log.debug(__name__)
    seats = get_seats()

    print(f"Highest found: {max(seats)}")
    print(f"My seat number: {find_empty(seats)}")
