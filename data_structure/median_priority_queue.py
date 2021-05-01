import pathmagic  # noqa
from data_structure.min_heap import MinHeap
from data_structure.max_heap import MaxHeap


class MedianPriorityQueue:
    def __init__(self, capacity: int):
        if capacity % 2 == 0:
            self.left = MaxHeap(capacity)
            self.right = MinHeap(capacity)
        else:
            self.left = MaxHeap(capacity + 1)
            self.right = MinHeap(capacity + 1)

    def add(self, data: int):
        if self.left.size == 0 and self.right.size == 0:
            self.left.insert(data)
        elif self.right.size == 0:
            self.right.insert(data)
        elif data > self.right.get_min():
            self.right.insert(data)
        else:
            self.left.insert(data)

        self.balance()

    def balance(self):
        if self.left.size - self.right.size >= 2:
            self.right.insert(self.left.remove_max())
        elif self.right.size - self.left.size >= 2:
            self.left.insert(self.right.remove_min())

    def remove(self):
        if self.left.size == 0:
            raise Exception("Priority Queue empty")

        if self.left.size >= self.right.size:
            data = self.left.remove_max()
        else:
            data = self.right.remove_min()

        self.balance()

        return data

    def peek(self):
        if self.left.size == 0 and self.right.size == 0:
            raise Exception("Priority Queue empty")

        if self.left.size >= self.right.size:
            return self.left.get_max()
        else:
            return self.right.get_min()

    def size(self):
        return self.left.size + self.right.size
