"""Problem Statement
https://leetcode.com/problems/single-number-ii/
"""
from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        maximum = max(nums)
        three_n = ((~maximum) | maximum)
        three_n_plus_1 = 0
        three_n_plus_2 = 0

        for num in nums:
            common_w_three_n = num & three_n
            common_w_three_n_plus_1 = num & three_n_plus_1
            common_w_three_n_plus_2 = num & three_n_plus_2

            three_n &= ~common_w_three_n
            three_n_plus_1 |= common_w_three_n

            three_n_plus_1 &= ~common_w_three_n_plus_1
            three_n_plus_2 |= common_w_three_n_plus_1

            three_n_plus_2 &= ~common_w_three_n_plus_2
            three_n |= common_w_three_n_plus_2

        return three_n_plus_1


if __name__ == "__main__":
    arr = [0, 1, 0, 1, 0, 1, 99]
    test = Solution()
    print(test.singleNumber(arr))
