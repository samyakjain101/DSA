"""Problem Statement
https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
"""


class Solution:

    def powerOf2(self, n):
        power = 0

        while (1 << power) <= n:
            power += 1

        return power - 1

    def countSetBits(self, n):
        if n == 0:
            return 0

        x = self.powerOf2(n)

        two_to_pow_x = 1 << x
        answer = ((two_to_pow_x >> 1) * x) + (n - two_to_pow_x + 1) + self.countSetBits(n - two_to_pow_x)
        return int(answer)


if __name__ == "__main__":
    n = 18
    test = Solution()
    print(test.countSetBits(n))
