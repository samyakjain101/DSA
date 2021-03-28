"""Problem Statement

https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/triplets-1-official/ojquestion#

"""


def solve(array):
    triplets = 0
    for i in range(len(arr)-1):
        xor = array[i]
        for k in range(i+1, len(arr)):
            xor ^= array[k]
            if xor == 0:
                triplets += k - i

    return triplets


if __name__ == "__main__":
    N = int(input())
    arr = []
    try:
        arr = list(map(int, input().split()))
        if len(arr) != N:
            raise ValueError
    except ValueError:
        for _ in range(N-1):
            arr.append((int(input())))

    print(solve(arr))
