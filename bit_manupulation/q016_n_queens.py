"""Problem Statement
https://leetcode.com/problems/sudoku-solver/
"""
from typing import List


result = []


class Solution:

    def solve(self, n, i, cols, diagonals, diagonals_reverse, board, answer) -> None:
        if i == n:
            temp = []
            for row in board:
                temp.append("".join(row))
            answer.append(temp)
            return

        for k in range(n):
            if ((cols & (1 << k)) == 0 and
                    (diagonals & (1 << i+k)) == 0 and
                    (diagonals_reverse & (1 << i-k+n-1)) == 0):

                board[i][k] = 'Q'
                cols ^= (1 << k)
                diagonals ^= (1 << i+k)
                diagonals_reverse ^= (1 << i-k+n-1)

                self.solve(n, i+1, cols, diagonals, diagonals_reverse, board, answer)

                board[i][k] = '.'
                cols ^= (1 << k)
                diagonals ^= (1 << i + k)
                diagonals_reverse ^= (1 << i - k + n - 1)

    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = 0
        diagonals = 0
        diagonals_reverse = 0

        board = [['.']*n for _ in range(n)]
        answer = list()

        self.solve(n, 0, cols, diagonals, diagonals_reverse, board, answer)
        return answer


if __name__ == "__main__":
    board_size = 4
    test = Solution()
    print(test.solveNQueens(board_size))
