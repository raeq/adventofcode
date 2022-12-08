import string

from anytree import NodeMixin, Node, search

TEST = False

if TEST:
    fn = "day07_test.txt"
else:
    fn = "day07.txt"


class FS_Dir(NodeMixin):
    def __init__(self, name: str, size: int = 0, parent: Node = None, children: Node = None):
        if children:
            self.children = children
        if parent:
            self.parent = parent
        self.name = name
        self._size = size

    @property
    def ftype(self) -> str:
        return "dir"

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = int(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', size={self.size}, ftype='{self.ftype}')"


class FS_File(NodeMixin):
    def __init__(self, name: str, size: int = 0, parent: FS_Dir = None):
        if parent:
            self.parent = parent
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', size={self.size}, ftype='{self.ftype}')"

    @property
    def ftype(self) -> str:
        return "file"

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = int(value)

        # update every ancestor
        for p in self.ancestors:
            p.size += value


root: FS_Dir = FS_Dir("/")

with open(fn) as f:
    current_dir = root

    for num, line in enumerate(f.readlines(), 1):

        line = line.rstrip()
        data = line.split(" ")

        if line.startswith(tuple(string.digits)):
            fs: FS_File = FS_File(data[1], int(data[0]), parent=current_dir)
        elif line.startswith("dir "):
            fs: FS_Dir = FS_Dir(data[1], parent=current_dir)

        elif line.endswith("cd .."):
            current_dir = current_dir.parent

        elif line == "$ cd /":
            current_dir = root

        # at the current level, make a child the current node
        elif line.startswith("$ cd "):
            for n in current_dir.children:
                if n.name == data[2] and n.ftype == "dir":
                    current_dir = n

total = 0
all_small_dirs = list(search.findall(root, lambda node: node.size <= 100000))
for n in filter(lambda x: isinstance(x, FS_Dir), all_small_dirs):
    total += n.size

print(f"Day 1 part 1 answer: {total}")

used_disk = root.size
unused_space = 70_000_000 - used_disk
free_needed = 30_000_000 - unused_space

current_best = None
for n in filter(lambda x: isinstance(x, FS_Dir), search.findall(root)):
    if n.size >= free_needed:
        if not current_best or n.size < current_best.size:
            current_best = n

print(f"Day 1 part 2 answer: {current_best.size}")
