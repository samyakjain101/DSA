"""Problem Statement
https://leetcode.com/problems/sudoku-solver/
"""
from typing import List


class Solution:

    def backtrack(self, board, i, j, rows, cols, blocks):
        if j == len(board):
            return True

        if i < len(board[0]) - 1:
            next_i = i + 1
            next_j = j
        else:
            next_i = 0
            next_j = j + 1

        if board[i][j] != '.':
            if self.backtrack(board, next_i, next_j, rows, cols, blocks):
                return True
        else:
            for choice in range(1, 10):
                mask = 1 << choice
                if ((rows[i] & mask) == 0 and
                        (cols[j] & mask) == 0 and
                        (blocks[i//3][j//3] & mask) == 0):

                    board[i][j] = str(choice)
                    rows[i] ^= mask
                    cols[j] ^= mask
                    blocks[i // 3][j // 3] ^= mask

                    if self.backtrack(board, next_i, next_j, rows, cols, blocks):
                        return True
                    # backtrack
                    board[i][j] = '.'
                    rows[i] ^= mask
                    cols[j] ^= mask
                    blocks[i // 3][j // 3] ^= mask

    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0]*9
        cols = [0]*9
        blocks = [[0]*3 for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    mask = 1 << int(board[i][j])
                    rows[i] |= mask
                    cols[j] |= mask
                    blocks[i//3][j//3] |= mask

        self.backtrack(board, 0, 0, rows, cols, blocks)


if __name__ == "__main__":
    sudoku = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    test = Solution()
    test.solveSudoku(sudoku)
    print(sudoku)
