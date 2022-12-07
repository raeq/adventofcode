import string
from collections import deque

stacks = []
for i in range(9):
    stacks.append(deque())


def get_top_crate(s) -> str:
    ans = ""
    for stack in stacks:
        try:
            if stack[0]:
                ans += stack[0]
        except IndexError:
            ans += "-"
    return ans


with open("day05.txt") as f:
    for line in f.readlines():
        line = line.rstrip()

        try:
            if line[0] != "m":
                counter = 0
                for i in range(1, 35):
                    if line[i] in string.ascii_uppercase:
                        stacks[counter].append(line[i])
                    counter = i // 4

            elif line[0] == "m":

                instruction = line.split(" ")
                repeat, source, target = int(instruction[1]), int(instruction[3]) - 1, int(instruction[5]) - 1

                for i in range(repeat):
                    stacks[target].appendleft(stacks[source].popleft())

        except IndexError:
            ...

print(get_top_crate(stacks))

stacks = []
for i in range(9):
    stacks.append(deque())

with open("day05.txt") as f:
    for line in f.readlines():
        line = line.rstrip()

        try:
            if line[0] != "m":
                counter = 0
                for i in range(1, 35):
                    if line[i] in string.ascii_uppercase:
                        stacks[counter].append(line[i])
                    counter = i // 4

            elif line[0] == "m":

                instruction = line.split(" ")
                repeat, source, target = int(instruction[1]), int(instruction[3]) - 1, int(instruction[5]) - 1

                temp_deq: deque = deque()
                for i in range(repeat):
                    temp_deq.append(stacks[source].popleft())

                while temp_deq:
                    stacks[target].appendleft(temp_deq.pop())


        except IndexError:
            ...

print(get_top_crate(stacks))
