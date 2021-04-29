import pathmagic # noqa
from data_structure.base_heap import HeapBase


class MinHeap(HeapBase):

    def insert(self, data: int):
        if self.is_full():
            raise Exception("Heap is full")

        self.storage[self.size] = data
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.storage[index]:
            parent_index = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index

    def remove_min(self):
        if self.size == 0:
            raise Exception("Heap is empty")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return data

    def heapify_down(self):
        index = 0

        while self.has_left_child(index):
            smaller_child_index = (
                self.get_left_child_index(index)
                if self.left_child(index) < self.right_child(index)
                else self.get_right_child_index(index)
            )

            if self.storage[smaller_child_index] < self.storage[index]:
                self.swap(smaller_child_index, index)
                index = smaller_child_index
            else:
                break

    def get_min(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        return self.storage[0]


if __name__ == "__main__":
    min_heap = MinHeap(3)
    min_heap.insert(10)
    min_heap.insert(-99)
    min_heap.insert(50)
    print(min_heap.get_min())
    print(min_heap.remove_min())
    print(min_heap.remove_min())
    min_heap.insert(0)
    print(min_heap.remove_min())
