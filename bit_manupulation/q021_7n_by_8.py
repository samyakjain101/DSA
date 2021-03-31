"""Problem Statement
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/solve-7nby8-official/ojquestion
"""


class Solution:
    def solve(self, n: int) -> int:
        """
        7 * n / 8 = (8 * n - n) / 8
        """
        return ((n << 3) - n) >> 3


if __name__ == "__main__":
    num = 16
    test = Solution()
    print(test.solve(num))
