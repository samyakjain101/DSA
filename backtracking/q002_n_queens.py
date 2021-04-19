"""Problem Statement
https://leetcode.com/problems/sudoku-solver/
"""
from typing import List


class Solution:
    def solve(self, n, i, cols, diagonals, diagonals_reverse, board, answer) -> None:
        if i == n:
            temp = []
            for row in board:
                temp.append("".join(row))
            answer.append(temp)
            return

        for k in range(n):
            if cols[k] and diagonals[i + k] and diagonals_reverse[i - k + n - 1]:
                board[i][k] = "Q"
                cols[k] = False
                diagonals[i + k] = False
                diagonals_reverse[i - k + n - 1] = False

                self.solve(n, i + 1, cols, diagonals, diagonals_reverse, board, answer)

                board[i][k] = "."
                cols[k] = True
                diagonals[i + k] = True
                diagonals_reverse[i - k + n - 1] = True

    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [True] * n
        diagonals = [True] * (2 * n - 1)
        diagonals_reverse = [True] * (2 * n - 1)

        board = [["."] * n for _ in range(n)]
        answer = list()

        self.solve(n, 0, cols, diagonals, diagonals_reverse, board, answer)
        return answer


if __name__ == "__main__":
    board_size = 4
    test = Solution()
    print(test.solveNQueens(board_size))
