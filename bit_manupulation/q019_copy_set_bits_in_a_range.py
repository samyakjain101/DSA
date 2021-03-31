"""Problem Statement
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/copy-set-bits-in-a-range-official/ojquestion
"""


class Solution:

    def copySetBitsInRange(self, A, B, left, right):
        mask = (2 ** (right - left + 1) - 1) << (left - 1)
        B |= mask & A
        return B


if __name__ == "__main__":
    A = int(input())
    B = int(input())
    left = int(input())
    right = int(input())
    test = Solution()
    print(test.copySetBitsInRange(A, B, left, right))
