import pathmagic  # noqa
from data_structure.min_heap import MinHeap


def sort_k_nearly_sorted(array: list, k: int):
    heap = MinHeap(k + 1)
    i = 0
    while i < k + 1:
        heap.insert(array[i])
        i += 1

    j = 0
    n = len(array)
    while j < len(array):
        array[j] = heap.remove_min()
        j += 1

        if i < n:
            heap.insert(array[i])
            i += 1

    return array


if __name__ == "__main__":
    arr = [3, 2, 4, 1, 6, 5, 7, 9, 8]
    k = 3
    print(sort_k_nearly_sorted(arr, k))
