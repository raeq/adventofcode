from collections import deque

import pandas as pd

df = pd.read_fwf("day12.txt", header=None, widths=[1] * 167)
letters = df.values.tolist()

df = df.applymap(lambda x: ord(x) - ord('a') + 1)
elevations = df.values.tolist()

row_count = len(letters)
col_count = len(letters[0])


def bfs(part):
    path = deque()
    for row, row_list in enumerate(letters):
        for col, val in enumerate(row_list):
            if val == 'S':
                elevations[row][col] = 1
            if val == 'E':
                elevations[row][col] = 26

            # add starting points at distance of 0
            if (part == 1 and val == 'S') or (part == 2 and elevations[row][col] == 1):
                path.append(((row, col), 0))

    backtrack = set()

    while path:
        (row, col), distance = path.popleft()

        if letters[row][col] == 'E':
            return distance

        if (row, col) not in backtrack:
            backtrack.add((row, col))

            for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row = row + delta_row
                new_col = col + delta_col

                if 0 <= new_row < row_count and 0 <= new_col < col_count:  # new coordinates are within bounds
                    if elevations[new_row][new_col] <= 1 + elevations[row][col]:  # new next choice is max 1 height
                        path.append(((new_row, new_col), distance + 1))


print(f'Day 12 part 1 ans: {bfs(1)}')
print(f'Day 12 part 2 ans: {bfs(2)}')
