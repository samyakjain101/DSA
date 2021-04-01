"""Problem Statement
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(32):
            if (1 << i) & n:
                answer |= 1 << (31 - i)

        return answer


if __name__ == "__main__":
    N = 0b11111111111111111111111111111101
    test = Solution()
    print(test.reverseBits(N))
