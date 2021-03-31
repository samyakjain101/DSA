"""Problem Statement
https://practice.geeksforgeeks.org/problems/bit-difference-1587115620/1
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
