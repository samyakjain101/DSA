"""Problem Statement
https://practice.geeksforgeeks.org/problems/swap-all-odd-and-even-bits-1587115621/1
"""


class Solution:
    def solve(self, n: int) -> int:
        even_mask = 0xAAAAAAAA
        odd_mask = 0x55555555

        even_mask &= n
        odd_mask &= n

        return (even_mask >> 1) | (odd_mask << 1)


if __name__ == "__main__":
    num = 23
    test = Solution()
    print(test.solve(num))
