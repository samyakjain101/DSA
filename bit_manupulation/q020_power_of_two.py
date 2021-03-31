"""Problem Statement
https://leetcode.com/problems/power-of-two/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        if n & (n-1) == 0:
            return True
        return False


if __name__ == "__main__":
    num = 16
    test = Solution()
    print(test.isPowerOfTwo(num))
