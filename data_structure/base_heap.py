class HeapBase:
    def __init__(self, capacity: int):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    @staticmethod
    def get_parent_index(index: int):
        return (index - 1) // 2

    @staticmethod
    def get_left_child_index(index: int):
        return 2 * index + 1

    @staticmethod
    def get_right_child_index(index: int):
        return 2 * index + 2

    def has_parent(self, index: int):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index: int):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index: int):
        return self.get_right_child_index(index) < self.size

    def is_full(self):
        return self.size == self.capacity

    def swap(self, index1: int, index2: int):
        self.storage[index1], self.storage[index2] = (
            self.storage[index2],
            self.storage[index1],
        )

    def parent(self, index: int):
        return self.storage[self.get_parent_index(index)]

    def left_child(self, index: int):
        return self.storage[self.get_left_child_index(index)]

    def right_child(self, index: int):
        return self.storage[self.get_right_child_index(index)]
