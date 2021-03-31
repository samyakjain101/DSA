"""Problem Statement
https://leetcode.com/problems/single-number-ii/
"""
from q002_kernighans_algo import kernighans


class Solution:

    def countBitsFlip(self, a, b):
        return kernighans(a ^ b)


if __name__ == "__main__":
    num1 = 10
    num2 = 20
    test = Solution()
    print(test.countBitsFlip(num1, num2))
