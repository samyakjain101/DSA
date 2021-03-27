"""Problem statement
https://leetcode.com/problems/single-number-iii/
"""
from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:

        if len(nums) == 2:
            return nums

        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Rightmost set bit mask of xor_all
        mask = xor_all & -xor_all

        xor_group0 = xor_group1 = 0
        for num in nums:
            if mask & num != 0:
                xor_group1 ^= num
            else:
                xor_group0 ^= num

        return [xor_group0, xor_group1]


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]

    test = Solution()
    print(test.singleNumber(nums))
