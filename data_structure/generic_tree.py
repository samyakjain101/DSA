from collections import deque


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

        print(f"{data} -> {childrens_data}")

        for child in childrens:
            self._display(child)

    def total_nodes(self, node=None):
        if node is None:
            node = self.root

        total = 1
        for child in node.childrens:
            total += self.total_nodes(child)

        return total

    def maximum(self, node=None):
        if node is None:
            node = self.root

        maximum = node.data
        for child in node.childrens:
            maximum = max(self.maximum(child), maximum)

        return maximum

    def height(self, node=None):
        if node is None:
            node = self.root

        height = 0
        for child in node.childrens:
            height = max(1 + self.height(child), height)

        return height

    def traversal(self, node=None):
        if node is None:
            node = self.root

        print(f"Node Pre {node.data}")
        for child in node.childrens:
            print(f"Edge Pre {node.data}--{child.data}")
            self.traversal(child)
            print(f"Edge Post {node.data}--{child.data}")
        print(f"Node Post {node.data}")

    def level_order_traversal(self):
        q = deque()
        q.append(self.root)

        while len(q):
            poped_node = q.popleft()
            print(poped_node.data)
            q += poped_node.childrens

    def level_order_linewise(self):
        traverse = [self.root]

        while len(traverse):
            new_traverse = []
            for node in traverse:
                new_traverse += node.childrens

            print(*[node.data for node in traverse])
            traverse = new_traverse

    def level_order_zig_zag(self):
        left_to_right = True
        traverse = [self.root]

        while traverse:
            new_traverse = []
            for node in traverse:
                new_traverse += node.childrens

            print(*[node.data for node in traverse])

            if left_to_right:
                traverse = new_traverse[::-1]
                left_to_right = False
            else:
                traverse = new_traverse
                left_to_right = True

    def mirror_tree(self):
        traverse = [self.root]

        while traverse:
            new_traverse = []
            for node in traverse:
                new_traverse += node.childrens

            i = 0
            j = len(new_traverse) - 1
            while i < j:
                new_traverse[i].data, new_traverse[j].data = (
                    new_traverse[j].data,
                    new_traverse[i].data,
                )
                i += 1
                j -= 1

            traverse = new_traverse

    def mirror_recursive(self, node=None):
        if node is None:
            node = self.root

        for child in node.childrens:
            self.mirror_recursive(node=child)

        if node.childrens:
            node.childrens = node.childrens[::-1]

    def remove_leaves(self, node=None):
        if node is None:
            node = self.root

        new_childrens = []
        for child in node.childrens:

            if child.childrens:
                new_childrens.append(child)
                self.remove_leaves(node=child)

        node.childrens = new_childrens


if __name__ == "__main__":
    # tree_euler = [
    #     10, 20, 50, -1, 60, -1, -1, 30,
    #     70, -1, 80, 110, -1, 120, -1, -1,
    #     90, -1, -1, 40, 100, -1, -1, -1]

    tree_euler = [10, 20, -1, 30, 50, -1, 60, -1, -1, 40, -1, -1]
    tree = GenericTree(tree_euler)
    tree.display()
    # print(f'Total nodes: {tree.total_nodes()}')
    # print(f'Maximum in tree: {tree.maximum()}')
    # print(f'Height of tree: {tree.height()}')
    # tree.traversal()
    # tree.level_order_traversal()
    # print('\nLevel order linewise traversal:')
    # tree.level_order_linewise()
    # print('\nLevel order traversal zigzag:')
    # tree.level_order_zig_zag()
    # tree.mirror_tree()
    # tree.mirror_recursive()
    tree.remove_leaves()
    tree.display()