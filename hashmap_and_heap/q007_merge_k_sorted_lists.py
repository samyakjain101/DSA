import pathmagic  # noqa
from data_structure.min_heap import MinHeap


def merge_k_sorted_lists(arrays: list):
    k = len(arrays)
    pointer = [0]*k
    heap = MinHeap(k)

    helper_hash = dict()
    for idx, value in enumerate(pointer):
        data = arrays[idx][value]
        helper_hash[data] = idx
        heap.insert(data)

    merged_array = []
    while heap.size != 0:
        removed_data = heap.remove_min()
        idx = helper_hash[removed_data]
        pointer[idx] += 1
        if pointer[idx] < len(arrays[idx]):
            data = arrays[idx][pointer[idx]]
            helper_hash[data] = idx
            heap.insert(data)

        helper_hash.pop(removed_data)
        merged_array.append(removed_data)

    return merged_array


if __name__ == "__main__":
    k = int(input())
    arrays = []

    for _ in range(k):
        n = int(input())
        arr = list(map(int, input().split()))
        arrays.append(arr)

    print(merge_k_sorted_lists(arrays))
