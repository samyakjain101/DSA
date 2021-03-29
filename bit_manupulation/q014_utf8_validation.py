"""Problem Statement

https://leetcode.com/problems/utf-8-validation/

"""
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        start_next_with_10 = 0

        for val in data:
            if not start_next_with_10:
                if (val >> 7) == 0b0:
                    continue
                elif (val >> 5) == 0b110:
                    start_next_with_10 += 1
                elif (val >> 4) == 0b1110:
                    start_next_with_10 += 2
                elif (val >> 3) == 0b11110:
                    start_next_with_10 += 3
                else:
                    return False
            else:
                if (val >> 6) == 0b10:
                    start_next_with_10 -= 1
                else:
                    return False

        return True if not start_next_with_10 else False


if __name__ == "__main__":
    arr = [197, 130, 1]
    test = Solution()
    print(test.validUtf8(arr))
