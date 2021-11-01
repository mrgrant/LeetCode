#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, k):
            for i in range(9):
                if k == board[row][i]:
                    return False
                if k == board[i][col]:
                    return False
                if k == board[row // 3 * 3 + i % 3][col // 3 * 3 + i // 3]:
                    return False
            return True

        def dfs():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in range(1, 10):
                            if isValid(board, i, j, str(k)):
                                board[i][j] = str(k)
                                if dfs():
                                    return True
                                else:
                                    board[i][j] = "."
                        return False 
            return True
        dfs()


        
# @lc code=end

