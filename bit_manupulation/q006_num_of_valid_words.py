"""Problem statement
https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
"""
from typing import List


class Solution:

    def get_mask(self, word):

        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord('a'))

        return mask

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        mask_frequencies = {}
        for word in words:
            mask = self.get_mask(word)
            mask_frequencies[mask] = mask_frequencies.get(mask, 0) + 1

        answer = [0]*len(puzzles)
        for idx, puzzle in enumerate(puzzles):
            puzzle_mask = self.get_mask(puzzle)
            sub_mask = puzzle_mask
            puzzle_first_letter_bit = ord(puzzle[0]) - ord('a')
            while sub_mask != 0:

                # first letter of puzzle in word
                if (1 << puzzle_first_letter_bit) & sub_mask != 0:
                    answer[idx] += mask_frequencies.get(sub_mask, 0)

                sub_mask = (sub_mask - 1) & puzzle_mask

        return answer


if __name__ == "__main__":
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]

    test = Solution()
    print(test.findNumOfValidWords(words, puzzles))
