"""Problem Statement
https://practice.geeksforgeeks.org/problems/find-sum-of-different-corresponding-bits-for-all-pairs4652/1
"""


class Solution:
    def countBits(self, N, A):

        answer = 0
        for i in range(32):
            set_bits = 0
            for num in A:
                if num & (1 << i) != 0:
                    set_bits += 1
            unset_bits = N - set_bits

            answer += 2 * (set_bits * unset_bits)

        return answer % (10 ** 9 + 7)


if __name__ == "__main__":
    arr = [1, 3, 5]
    n = len(arr)
    test = Solution()
    print(test.countBits(n, arr))
