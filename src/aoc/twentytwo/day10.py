total = 0
cycle = 1
x = 1
crt = []
row = ''

with open("day10.txt") as fin:
    for instr in fin:
        row += '#' if x <= cycle % 40 < x + 3 else ' '
        cycle += 1

        if instr.startswith('addx'):
            if cycle % 40 == 20:
                total += cycle * x
            elif cycle % 40 == 1:
                crt.append(row)
                row = ''

            row += '#' if x <= cycle % 40 < x + 3 else ' '
            cycle += 1
            x += int(instr[5:])

        if cycle % 40 == 20:
            total += cycle * x
        elif cycle % 40 == 1:
            crt.append(row)
            row = ''

print(1, total)
print('Part 2:\n', '\n'.join(crt), sep='')
