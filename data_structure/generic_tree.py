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

    def remove_leaves_without_using_extra_space(self, node=None):
        if node is None:
            node = self.root

        i = len(node.childrens) - 1
        while i >= 0:
            child = node.childrens[i]
            if child.childrens:
                self.remove_leaves_without_using_extra_space(node=child)
            else:
                node.childrens.pop(i)
            i -= 1

    @staticmethod
    def __get_tail(node):
        tail = node
        while tail.childrens:
            tail = tail.childrens[0]

        return tail

    def linearize_tree(self, node=None):
        if node is None:
            node = self.root

        for child in node.childrens:
            self.linearize_tree(node=child)

        while len(node.childrens) > 1:
            last_child = node.childrens.pop()
            second_last = node.childrens[-1]
            second_last_tail = self.__get_tail(second_last)
            second_last_tail.childrens = [last_child]

    def linearize_tree_optimized(self, node=None):
        if node is None:
            node = self.root

        if not node.childrens:
            return node

        last_child_tail = self.linearize_tree_optimized(node=node.childrens[-1])
        while len(node.childrens) > 1:
            last_child = node.childrens.pop()
            second_last_child = node.childrens[-1]
            second_last_child_tail = self.linearize_tree_optimized(
                node=second_last_child
            )
            second_last_child_tail.childrens = [last_child]

        return last_child_tail

    def find_element(self, data, node=None):
        if node is None:
            node = self.root

        if node.data == data:
            return True

        for child in node.childrens:
            if self.find_element(data, child):
                return True

        return False

    def node_to_root_path(self, data, node=None):
        if node is None:
            node = self.root

        if node.data == data:
            return [node.data]

        for child in node.childrens:
            result = self.node_to_root_path(data, child)
            if result:
                result.append(node.data)
                return result

        return []

    def lowest_common_ancestor(self, data1, data2):
        path1 = self.node_to_root_path(data1)
        path2 = self.node_to_root_path(data2)

        i, j = len(path1) - 1, len(path2) - 1
        while i >= 0 and j >= 0 and path1[i] == path2[j]:
            i -= 1
            j -= 1

        return path1[i + 1]

    def distance_between_nodes(self, data1, data2):
        path1 = self.node_to_root_path(data1)
        path2 = self.node_to_root_path(data2)

        i, j = len(path1) - 1, len(path2) - 1
        while i >= 0 and j >= 0 and path1[i] == path2[j]:
            i -= 1
            j -= 1

        return i + 1 + j + 1

    def is_symmetic(self, node=None):
        """Symmetric tree is mirror image of itself."""
        if node is None:
            node = self.root

        return mirror_in_shape(node, node)

    max_value = float("-inf")
    min_value = float("inf")
    height_tree = 0
    size_tree = 0

    def multisolver(self, node=None, depth=0):
        if node is None:
            node = self.root

        self.max_value = max(self.max_value, node.data)
        self.min_value = min(self.min_value, node.data)
        self.size_tree += 1
        self.height_tree = max(self.height_tree, depth)

        for child in node.childrens:
            self.multisolver(node=child, depth=depth + 1)

    predecessor = None
    successor = None
    state = 0

    def predecessor_and_successor(self, data, node=None):
        if node is None:
            node = self.root

        if self.state == 0:
            if node.data == data:
                self.state = 1
            else:
                self.predecessor = node.data
        elif self.state == 1:
            self.successor = node.data
            self.state = 2

        for child in node.childrens:
            self.predecessor_and_successor(data=data, node=child)

    ceil = float("inf")
    floor = float("-inf")

    def ceil_and_floor(self, data, node=None):
        if node is None:
            node = self.root

        if data < node.data < self.ceil:
            self.ceil = node.data
        if data > node.data > self.floor:
            self.floor = node.data

        for child in node.childrens:
            self.ceil_and_floor(data, node=child)


def similar_in_shape(root1, root2):
    n1, n2 = len(root1.childrens), len(root2.childrens)
    if n1 == n2:
        for i in range(n1):
            if not similar_in_shape(root1.childrens[i], root2.childrens[i]):
                return False
    else:
        return False

    return True


def mirror_in_shape(root1, root2):
    n1, n2 = len(root1.childrens), len(root2.childrens)
    if n1 == n2:
        for i in range(n1):
            if not similar_in_shape(root1.childrens[i], root2.childrens[n1 - i - 1]):
                return False
    else:
        return False

    return True


if __name__ == "__main__":
    # tree_euler = [
    #     10,
    #     20,
    #     50,
    #     -1,
    #     60,
    #     -1,
    #     -1,
    #     30,
    #     70,
    #     -1,
    #     80,
    #     110,
    #     -1,
    #     120,
    #     -1,
    #     -1,
    #     90,
    #     -1,
    #     -1,
    #     40,
    #     100,
    #     -1,
    #     -1,
    #     -1,
    # ]

    tree_euler = [10, 20, -1, 30, 50, -1, 60, -1, -1, 40, -1, -1]
    tree = GenericTree(tree_euler)
    # tree.display()
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
    # tree.remove_leaves()
    # tree.remove_leaves_without_using_extra_space()
    # tree.linearize_tree()
    # tree.linearize_tree_optimized()
    # tree.display()
    # print(tree.node_to_root_path(0))
    # print(tree.lowest_common_ancestor(70, 110))
    # print(tree.distance_between_nodes(70, 110))
    # tree2 = GenericTree(tree_euler)
    # print(similar_in_shape(tree.root, tree2.root))
    # mirror_euler = [
    #     10,
    #     40,
    #     100,
    #     -1,
    #     -1,
    #     30,
    #     90,
    #     -1,
    #     80,
    #     120,
    #     -1,
    #     110,
    #     -1,
    #     -1,
    #     70,
    #     -1,
    #     -1,
    #     20,
    #     60,
    #     -1,
    #     80,
    #     -1,
    #     -1,
    #     -1,
    # ]
    # mirror_tree = GenericTree(mirror_euler)
    # print(mirror_in_shape(tree.root, mirror_tree.root))
    # print(tree.is_symmetic())
    # tree.multisolver()
    # print(
    #     {
    #         "max": tree.max_value,
    #         "min": tree.min_value,
    #         "size": tree.size_tree,
    #         "height": tree.height_tree,
    #     }
    # )
    # tree.predecessor_and_successor(50)
    # print({"predecessor": tree.predecessor, "successor": tree.successor})
    tree.ceil_and_floor(data=50)
    print({"ceil": tree.ceil, "floor": tree.floor})
