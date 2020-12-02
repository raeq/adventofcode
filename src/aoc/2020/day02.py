"""
Part 1
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number
of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times.

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
but needs at least 1. The first and third passwords are valid: they contain one a or nine c,
both within the limits of their respective policies.

How many passwords are valid according to their policies?

Part 2
Each policy actually describes two positions in the password, where 1 means the first character, 2 means
the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant
for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

"""


def get_data(filename: str) -> list:
    return_list: list = []

    with open(filename, 'r') as f:
        for line in f:
            return_list.append(tuple(line.split()))

    return return_list


def check_passwords(passwords: list) -> tuple:
    my_count1 = 0
    my_count2 = 0

    for t in tuple(passwords):
        split = t[0].split("-")
        start = int(split[0])
        end = int(split[1])

        letter: str = t[1][:1]
        password = t[2]

        c = password.count(letter)
        if start <= c <= end:
            my_count1 += 1

        positions = password[start - 1] + password[end - 1]
        if (letter in (positions[0], positions[1])) and positions[0] != positions[1]:
            my_count2 += 1

    return my_count1, my_count2


results = check_passwords(get_data("day02.txt"))
print(f"There are {results[0]} passwords conforming to the first part of the Day 02 question.")
print(f"There are {results[1]} passwords conforming to the second part of the Day 02 question.")
