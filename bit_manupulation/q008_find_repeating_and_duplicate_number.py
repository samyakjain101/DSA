"""Problem statement
https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
"""


class Solution:
    def findTwoElement(self, arr, n):
        xor_all = 0
        for num in arr:
            xor_all ^= num
        for i in range(1, n+1):
            xor_all ^= i

        # Now, xor_all = missing_number ^ duplicate_number
        # find rightmost set bit mask of xor_all
        mask = xor_all & -xor_all

        group0 = group1 = 0
        for num in arr:
            if mask & num != 0:
                group1 ^= num
            else:
                group0 ^= num
        for i in range(1, n+1):
            if mask & i != 0:
                group1 ^= i
            else:
                group0 ^= i

        for num in arr:
            if num == group0:
                return [group0, group1]
            if num == group1:
                return [group1, group0]


if __name__ == "__main__":
    arr = [1, 3, 3]
    n = 3

    test = Solution()
    print(test.findTwoElement(arr, n))
