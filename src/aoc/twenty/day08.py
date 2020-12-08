import typing
from collections import namedtuple as nt

import matplotlib.pyplot as plt
import networkx as nx

Instruction: nt = nt('Instruction', ['seq', 'opcode', 'operand', 'hits'])
Execution: nt = nt('Execution', ['step', 'register', 'previous_i', 'next_i', 'instruction'])
instruction_set: typing.List[Instruction] = []


def load_file(file_name: str) -> typing.List[Instruction]:
    c: int = 0
    with open(file_name, "r") as fd:
        for line in fd.readlines():
            splitted = line.rstrip("\n").split()
            instruction_set.append(Instruction(seq=c, opcode=splitted[0], operand=int(splitted[1]), hits=0))
            c += 1
    return instruction_set


def execute_program(instructions: list):
    e: Execution
    n: int = 0
    c: int = 1
    r: int = 0
    run_list: typing.List[Execution] = []
    i: Instruction

    while n < len(instructions):

        instructions[n] = instructions[n]._replace(hits=instructions[n].hits + 1)
        i = instructions[n]

        if i.hits < 2:

            if i.opcode == "nop":
                e = Execution(step=c, register=r, next_i=n + 1, previous_i=n, instruction=i)
            if i.opcode == "jmp":
                e = Execution(step=c, register=r, next_i=n + i.operand, previous_i=n, instruction=i)
            if i.opcode == "acc":
                r += i.operand
                e = Execution(step=c, register=r, next_i=n + 1, previous_i=n, instruction=i)

            run_list.append(e)
            n = e.next_i
            c += 1
            print(e)

        else:
            print("halted")
            n = 20000

    return r, run_list


def main():
    program: typing.List[Instruction] = load_file("day08.txt")
    print(program)

    bp, run_list = execute_program(program)
    print(f"Part 1 complete with the register value at {bp}")


if __name__ == '__main__':
    main()


def build_graph(run_list: []):
    labelsdict: dict = {}
    G = nx.Graph()

    r: Execution
    for r in run_list:
        name: str = r.instruction.seq
        G.add_node(name, label=r.instruction.opcode + ' ' + str(r.instruction.operand))
        G.add_edge(name, r.next_i)
        G.add_edge(name, r.previous_i)
        labelsdict[name] = str(name) + '\n' + r.instruction.opcode + '\n' + str(r.instruction.operand)

    options = {
        "font_size": 8,
        "node_size": 800,
        "node_color": "white",
        "edgecolors": "red",
        "linewidths": 2,
        "width": 1,
        'font_color': "black",
        "with_labels": True,
        "label": "aoc 2020 / 07"
    }

    pos = nx.spring_layout(G, k=0.05, iterations=150)

    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.axis('equal')
    plt.figure(figsize=(12, 8), dpi=300)
    plt.plot()
    nx.draw(G, pos, labels=labelsdict, **options)
    plt.show()

    return G, labelsdict
