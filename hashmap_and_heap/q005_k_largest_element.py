import pathmagic # noqa
from data_structure.min_heap import MinHeap


def k_largest(array: list, k: int):
    heap = MinHeap(4)
    i = 0
    while i < k:
        heap.insert(array[i])
        i += 1

    n = len(array)
    while i < n:
        if heap.get_min() < array[i]:
            heap.remove_min()
            heap.insert(array[i])

        i += 1

    return heap.storage


if __name__ == "__main__":
    arr = [12, 62, 22, 15, 37, 99, 11, 37, 98, 67, 31, 84, 99]
    print(k_largest(arr, 4))
