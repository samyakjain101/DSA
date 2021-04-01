"""Problem Statement
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/min-xor-pairs-official/ojquestion
"""


def minXorPairs(n, nums):
    nums.sort()

    pairs = []
    mini = float('inf')
    for i in range(n-1):
        xor = nums[i]^nums[i+1]
        if xor < mini:
            mini = xor
            pairs = [[nums[i], nums[i+1]]]
        elif xor == mini:
            pairs.append([nums[i], nums[i+1]])

    return pairs


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    for pair in minXorPairs(N, arr):
        print(f'{pair[0]}, {pair[1]}')
