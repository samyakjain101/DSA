class Node:
    def __init__(self, data):
        self.data = data
        self.childrens = list()


class GenericTree:
    def __init__(self, euler):
        self.root = None
        self.generate_tree(euler)

    def generate_tree(self, euler):
        node_stack = []

        for data in euler:
            if data == -1:
                node_stack.pop()
            else:
                if self.root is None:
                    self.root = Node(data)
                    node_stack.append(self.root)
                    continue

                node = Node(data)
                node_stack[-1].childrens.append(node)
                node_stack.append(node)

    def display(self):
        self._display(self.root)

    def _display(self, node):
        data = node.data
        childrens = node.childrens
        childrens_data = [child.data for child in childrens]

        print(f'{data} -> {childrens_data}')

        for child in childrens:
            self._display(child)


if __name__ == "__main__":
    tree_euler = [
        10, 20, 50, -1, 60, -1, -1, 30,
        70, -1, 80, 110, -1, 120, -1, -1,
        90, -1, -1, 40, 100, -1, -1, -1]
    tree = GenericTree(tree_euler)
    tree.display()
