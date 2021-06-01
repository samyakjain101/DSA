import math


class SegmentTree:
    def __init__(self, array: list):
        self.__n = len(array)
        if self.__n % 2 == 0:
            size = self.__n * 2 - 1
        else:
            size = (1 << math.ceil(math.sqrt(self.__n))) * 2 - 1

        self.__tree = [float("inf")] * size
        self.__build_segment_tree(array, 0, self.__n - 1)

    def __build_segment_tree(self, array: list, low: int, high: int, pos: int = 0):
        if low == high:
            self.__tree[pos] = array[low]
            return

        mid = low + (high - low) // 2

        self.__build_segment_tree(array, low, mid, 2 * pos + 1)
        self.__build_segment_tree(array, mid + 1, high, 2 * pos + 2)

        self.__tree[pos] = min(self.__tree[2 * pos + 1], self.__tree[2 * pos + 2])

    def query_min(self, low: int, high: int):
        if low > high:
            raise Exception("low can't be greater than high")

        return self.__query_min_helper(low, high, 0, self.__n - 1)

    def __query_min_helper(
        self, qlow: int, qhigh: int, low: int, high: int, pos: int = 0
    ):
        if qlow <= low and high <= qhigh:
            return self.__tree[pos]
        if qlow > high or qhigh < low:
            return float("inf")

        mid = low + (high - low) // 2

        return min(
            self.__query_min_helper(qlow, qhigh, low, mid, 2 * pos + 1),
            self.__query_min_helper(qlow, qhigh, mid + 1, high, 2 * pos + 2),
        )


if __name__ == "__main__":
    data = [-1, 2, 4, 0]
    s = SegmentTree(data)
    print(s.query_min(3, 2))
