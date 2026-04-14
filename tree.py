class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        p = self.parent
        level = 0
        if p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        print(self.get_level() * " " + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
