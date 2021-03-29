"""Problem Statement

https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/pepcoder-and-bits-official/ojquestion

"""
from math import comb
from q002_kernighans_algo import kernighans


def count_bits(num):
    count = 0
    while num != 0:
        num >>= 1
        count += 1

    return count-1  # including 0-th index


def solve(num, k, i):
    if num == 0 or num == 1 or i == 0:
        return 0

    if num & (1 << i) == 0:
        return solve(num, k, i-1)
    else:
        temp = 0
        # Case 1: Set i-th bit as 0
        temp += comb(i, k)

        # Case 2: i-th bit remains 1
        temp += solve(num, k-1, i-1)
        return temp


if __name__ == "__main__":
    N = int(input())
    set_bits_count = kernighans(N)
    total_bits = count_bits(N)

    print(solve(N, set_bits_count, total_bits))
