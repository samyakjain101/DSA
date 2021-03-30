"""Problem Statement
https://leetcode.com/problems/sudoku-solver/
"""
from typing import List


class Solution:

    def isValid(self, board, choice, i, j):
        # check row
        for num in board[i]:
            if num == choice:
                return False

        # check col
        for check_i in range(0, len(board)):
            if board[check_i][j] == choice:
                return False

        # check block
        top_i = i // 3 * 3
        top_j = j // 3 * 3
        for check_i in range(top_i, top_i+3):
            for check_j in range(top_j, top_j+3):
                if board[check_i][check_j] == choice:
                    return False

        return True

    def solveSudoku(self, board: List[List[str]], i=0, j=0) -> bool:

        if j == len(board):
            return True

        if i < len(board[0]) - 1:
            next_i = i + 1
            next_j = j
        else:
            next_i = 0
            next_j = j + 1

        if board[i][j] != '.':
            if self.solveSudoku(board, next_i, next_j):
                return True
        else:
            for choice in range(1, 10):
                choice = str(choice)
                if self.isValid(board, choice, i, j):
                    board[i][j] = choice
                    if self.solveSudoku(board, next_i, next_j):
                        return True
                    board[i][j] = '.'


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
