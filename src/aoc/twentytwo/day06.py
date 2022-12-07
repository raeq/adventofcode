from collections import deque


def get_start_marker_position(message: str, seq_length: int = 4) -> int:
    the_stack: deque = deque(maxlen=seq_length)

    for sequence, char in enumerate(message):
        the_stack.append(char)

        if len(set(list(the_stack))) >= seq_length:
            return sequence + 1

    return 0


data = open("day06.txt").read().rstrip()
print(f"Day 6 part 1 answer: {get_start_marker_position(data)}")
print(f"Day 6 part 2 answer: {get_start_marker_position(data, 14)}")


def test_case1():
    assert get_start_marker_position("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_start_marker_position("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert get_start_marker_position("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert get_start_marker_position("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert get_start_marker_position("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
