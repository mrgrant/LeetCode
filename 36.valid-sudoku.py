#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            s1 = set()
            s2 = set()
            for j in range(9):
                if grid[i][j] != ".":
                    if grid[i][j] in s:
                        return False
                    s1.add(grid[i][j])
                if grid[j][i] != ".":
                    if grid[j][i] in s2:
                        return False
                    s2.add(grid[j][i]
        for i in range(3):
            for j in range(3):
                s = set()
                for m in range(3):
                    for n in range(3):
                        x = grid[3*i+m][3*j+n]
                        if x in s:
                            return False
                        s.add(x)
# @lc code=end

