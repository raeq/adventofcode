import networkx as nx
import pylab as plt


if __name__ == "__main__":

    with open("day12.txt") as f:
        CAVES = nx.Graph(line.split("-") for line in f.read().splitlines())


    def npaths(node, path, revisited):
        if node == "end": return 1

        return sum(
            npaths(neib, path | {node}, revisited | (neib.islower() and neib in path))
            for neib in CAVES[node]
            if neib != "start"
            if neib.isupper() or neib not in path or not revisited
        )


    print(npaths("start", set(), True))
    print(npaths("start", set(), False))

    nx.draw(CAVES, with_labels=True)
    plt.show()
